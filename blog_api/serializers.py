''' Serializer: it allow us to converted data in our database into easy and 
understadable way then we can render it into json  parse it back it to the our application i.e(React app) '''
from rest_framework import serializers
from blog.models import Post

 #this class extendig from serializers.ModelSerializer
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        #here we defied what data in model we want to work with
        fields = ('id', 'title', 'author', 'excerpt', 'content', 'status')
