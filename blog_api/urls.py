from django.urls import path
from .views import PostList, PostDetail 

app_name = 'blog_api'

#We are going to build two api end-point here

urlpatterns = [
    #this endpoint will used to show individual object from the database(this will show an individual post)
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    #this endpoint will used to show all the object and data from database(this will show all the post)
    path('', PostList.as_view(), name='listcreate'),

]