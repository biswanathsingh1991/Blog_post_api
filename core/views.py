from . serializers import UserProfileSerializer
from . models import UserProfile
from rest_framework.generics import ListAPIView, RetrieveAPIView


class AllUserProfile(ListAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class UserProfileDetailView(RetrieveAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
