from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import NotAuthenticated
from pyChatGPT import ChatGPT
from rest_framework.response import Response


class ChatGPTAPI(viewsets.GenericViewSet):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.api = None

    @action(detail=False, methods=['POST'], url_path='login')
    def login(self, request):
        """
        # auth with Google login
        self.api = ChatGPT(auth_type='google', email='example@gmail.com', password='password')

        # auth with microsoft login
        api = ChatGPT(auth_type='microsoft', email='example@gmail.com', password='password')

        # auth with openai login (manual captcha solving)
        api = ChatGPT(
            auth_type='openai', captcha_solver='',
            email='example@gmail.com', password='password'
        )
        """
        data = request.data
        self.api = ChatGPT(auth_type=data['auth_type'], email=data['email'], password=data['password'],
                           captcha_solver='')
        return Response("Login Successful", status=200)

    @action(detail=False, methods=['POST'], url_path='prompt')
    def prompt(self, request):
        data = request.data
        if not self.api:
            raise NotAuthenticated()

        resp = self.api.send_message(data['prompt'])
        print(resp['message'])
        return Response({"response": resp['message']}, status=200)
