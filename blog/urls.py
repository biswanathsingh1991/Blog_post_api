from django.urls import path
from .views import CreateView
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'blog'
urlpatterns = [
    # path('home/', HomeView.as_view(), name='home'),
    # path('creatblog/', Createblog.as_view(), name='createblog'),
    # path('updateblog/<int:pk>/', UpdateBlog.as_view(), name='updateblog'),
    # path('listblog/', ListBlog.as_view(), name='listblog'),
    # path('detailblogview/<int:pk>/', DetailBlogView.as_view(),
    #      name='detailblogview'),
    # path('deleteblogview/<int:pk>/', DeleteBlogView.as_view(),
    #      name='deleteblogview'),
    path('bucketlists/', CreateView.as_view(), name="create"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
