from django.db import models
#user going to make post thats why we import user from auth.models
from django.contrib.auth.models import User
#for Time Stamp
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Post(models.Model):
    #going to create model manager
    ''' By using this manager it will filter out only the posts whose status flag 
    is set to published given to the view'''
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    '''if any one try to delete the category then post should not delet
    thats why we used models.PROTECT to protect the post in the database
    we used foreign key to connect the category to the created post.'''
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

    title = models.CharField(max_length=250)
    excerpt = models.TextField()
    content = models.TextField()

    '''we are using slug here so that we can slugify the title, 
     we can utilizing this as a web identifying of each post. so instead of using the id for post
     we use slug to identify the collected the data'''
    slug = models.SlugField(max_length=250, unique_for_date='published')

    published = models.DateTimeField(default=timezone.now)

    '''we are using Cascade here so that if user who has made post if in future user
    got deleted then their related and created posts also be deleted.'''
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')


    #Draft mode of Posts
    status = models.CharField(max_length=10, choices=options, default='published')

    ''' here we specify the different model manager '''
    objects = models.Manager() #default manager
    postobjects = PostObjects() #Custom manager

    ''' we can return in ascending and descending order '''
    class Meta:
        ordering = ('-published', )

    def __str__(self):
        return self.title