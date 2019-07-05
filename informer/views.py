from django.http import HttpResponse
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView


class InformerView(APIView):
    def get(self, request):
        return Response({'commit': '000000'})
