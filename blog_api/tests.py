from django.test import TestCase
# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category
from django.contrib.auth.models import User

class PostTests(APITestCase):

    #1st Test Case
    def test_view_posts(self):
        #in our blog_api urls we have given app_name = blog_api and PostList name=listcreat
        url = reverse('blog_api:listcreate')
        #here client is a browser to simulating of browser and get request a url which is created above and data format in json format.  
        response = self.client.get(url, format='json')
        #we check our responses with http status code 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #2nd Test Case(data insertion checking in database, i.e create)
    def create_post(self):
        self.test_category = Category.objects.create(name='django')
        self.testuser1 = User.objects.create_user(username='test_user1', password='123456789')
        data = {"title": "new", "author": 1,
        "excerpt": "new", "content": "new"}
        url = reverse('blog_api:listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

