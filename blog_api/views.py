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
    pass
