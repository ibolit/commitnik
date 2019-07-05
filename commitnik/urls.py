from django.urls import include, path

urlpatterns = [
    path(
        'informer/',
        include(('informer.urls', 'informer'), namespace='informer')),
]
