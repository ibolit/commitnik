from django.contrib import admin
from django.urls import path

from informer.views import InformerView

urlpatterns = [
    path('informer', InformerView.as_view(), name='informer'),
]
