from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

class ExampleView(APIView):
    def get(self, request):
        return Response("Authenticated yay!")
