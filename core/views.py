
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.models import User
from django.views.generic import CreateView
from . models import UserProfile


class Home(TemplateView):

    template_name = 'core/home.html'


class UserCreation(CreateView):  # user creation generic view
    model = User
    template_name = 'core/usercreation.html'
    fields = "__all__"


# class UserProfileEdit(UpdateView):
#     model = UserProfile
#     template_name = "core/userprofile_edit.html"
#     fields = "__all__"
#     success_url = reverse_lazy('core:home')

#
# class UserDetailView(DetailView):
#     model = UserProfile
#     template_name = 'core/userdetailview.html'
#     context_object_name = 'object'
