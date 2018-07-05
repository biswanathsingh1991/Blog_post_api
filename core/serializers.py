from rest_framework import serializers
from .models import UserProfile, Adress, Friends


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = "__all__"


class AdressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adress
        fields = "__all__"


class FriendsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Friends
        fields = "__all__"
