from django.urls import path
from django.urls import include
from . views import AllUserProfile, UserProfileDetailView


urlpatterns = [

    path('alluserprofile/', AllUserProfile.as_view(), name="alluserprofile"),
    path('userprofiledetailview/<int:pk>/', UserProfileDetailView.as_view(), name="userprofiledetailview"),
]
