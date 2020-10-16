#from django.shortcuts import render
#we are going to used class based view here
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer

#now here our serializer class connected to ListCreateAPIView, then we collect all from the database
#and then translate by serializer in understandable mode.
class PostList(generics.ListCreateAPIView):
    #by using .postobjects it will give back all the posts that thas published flag.
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    pass

class PostDetail(generics.RetrieveDestroyAPIView):
    #it will give only a selected post by id that we have in a endpoint in urls.
    queryset = Post.objects.all()
    serializer_class = PostSerializer




""" Concrete View Classes
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
#ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
#RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""









