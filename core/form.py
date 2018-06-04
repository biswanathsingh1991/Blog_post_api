from djanog.form import ModelForm
from . models import UserProfile


class UserProfileEditForm(ModelForm):
    class meta:
        model = UserProfile
        fields = "__all__"
