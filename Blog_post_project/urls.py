from django.urls import path
from django.urls import include


urlpatterns = [

    path(r'^', include('blog.urls')),
]
