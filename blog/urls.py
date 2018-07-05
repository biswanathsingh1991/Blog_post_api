from django.urls import path
from django.shortcuts import include
from rest_framework import router

app_name = 'blog'
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))



    # commented
    # path('home/', HomeView.as_view(), name='home'),
    # path('creatblog/', Createblog.as_view(), name='createblog'),
    # path('updateblog/<int:pk>/', UpdateBlog.as_view(), name='updateblog'),
    # path('listblog/', ListBlog.as_view(), name='listblog'),
    # path('detailblogview/<int:pk>/', DetailBlogView.as_view(),
    #      name='detailblogview'),
    # path('deleteblogview/<int:pk>/', DeleteBlogView.as_view(),
    #      name='deleteblogview'),
    # path('bucketlists/', CreateView.as_view(), name="create"),
]
