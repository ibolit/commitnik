from django.http import HttpResponse
from django.views import View


class InformerView(View):
    def get(self, request):
        return HttpResponse('Hello, dude')
