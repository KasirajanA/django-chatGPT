import openai
import os

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


# Set up the OpenAI API credentials
openai.api_key = os.environ.get("OPENAI_API_KEY")


class ChatGPTAPI(viewsets.GenericViewSet):

    @action(detail=False, methods=['POST'], url_path='prompt')
    def prompt(self, request):
        data = request.data
        # Generate a response
        response = openai.Completion.create(
            engine="davinci",
            prompt=data["prompt"]
        )

        # Print the generated response
        print(response.choices[0].text)
        return Response({"response": response.choices[0].text}, status=200)
