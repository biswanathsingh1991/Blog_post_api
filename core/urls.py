from django.urls import path
from django.urls import include
from . views import AllUserProfile


urlpatterns = [

    path('alluserprofile/', AllUserProfile.as_view(), name="alluserprofile"),
]
