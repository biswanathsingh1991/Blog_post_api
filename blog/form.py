from django.forms import ModelForm
from . models import Blog


class CreateBlog(ModelForm):

    class Meta:
        model = Blog
        fields = "__all__"


class UpdateBlog(ModelForm):

    class Meta:
        model = Blog
        fields = "__all__"
