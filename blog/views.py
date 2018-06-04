from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . form import CreateBlog, UpdateBlog
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# Create your views here.


class HomeView(ListView):
    model = Blog
    template_name = 'blog/home.html'
    context_object_name = 'object_blog'


class Createblog(CreateView):
    model = Blog
    template_name = 'blog/create_blog.html'
    form_class = CreateBlog
    success_url = ''


class UpdateBlog(UpdateView):
    model = Blog
    form_class = UpdateBlog
    success_url = '/home'
    template_name = 'blog/update_blog.html'


# @login_required
class ListBlog(ListView):
    model = Blog
    template_name = 'blog/list_blog.html'
    context_object_name = 'list_blog'

    def get_queryset(self):
        return Blog.objects.filter(user=self.request.user)


class DetailBlogView(DetailView):
    model = Blog
    template_name = 'blog/detailblogview.html'
    context_object_name = 'detail_blog'


class DeleteBlogView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:listblog')
