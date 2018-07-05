from rest_framework import serializers
from . models import Blog, BlogComment, Like


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = "__all__"


class BlogCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogComment
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = "__all__"
