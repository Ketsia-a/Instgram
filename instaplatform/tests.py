from django.test import TestCase
from .models import Profile, Post, Comment
from django.contrib.auth.models import User
import datetimme as dt
# Create your tests here.

class ProfileTestClass(TestCase):
    '''
    images test method
    '''
    def setUp(self):
        self.user = User.objects.create(id =1,username='Ketsia')
        self.profile = Profile(username = 'lk203',bio = 'i dig in it',pp = 'highlight.jpeg',date = '05.10.2015', user = self.user)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))
    
    def test_save_method(self):
        '''
        test image by save
        '''
        self.profile.save_profile()
        profile=Profile.objects.all()
        self.assertTrue(len(profile)>=1) 
   
    def test_delete_method(self):
        '''
        test of delete image
        '''
        self.profile.save_profile()
        profile=Profile.delete_profile()
        profile=Profile.objects.all()
        self.assertTrue(len(profile)>=0) 

class CommentTestClass(TestCase):
    def setUp(self):
        self.comment=Comments.objects.create(comment='amazing one :)',created = '3.12.2018')

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comments))

    def test_save_method(self):
        '''
        test image by save
        '''
        self.comment.save_comments()
        comment=Comments.objects.all()
        self.assertTrue(len(comm)>0) 

    def test_delete_method(self):
        '''
        test of delete image
        '''
        self.comment.save_comments()
        self.comment.delete_comments()
        comment=Comments.objects.all()
        self.assertTrue(len(comm)>0)


class PostTestClass(TestCase):
    '''
    images test method
    '''
    def setUp(self):
        self.post = Post(image ='highlight.jpeg', name='beauty', caption='imagefsf',date='11.6.2020')
    
    def tearDown(self):
        Post.objects.all().delete()
        Profile.objects.all().delete()


        # Testing Instance
        def test_instance(self):
            self.assertTrue(isinstance(self.post,Post))


        # Testing the save method
        def test_save_method(self):
            self.post=Post(image_name='cat',description='beautiful',user=self.user1,show="image")
            self.post.save_post()
            images = Post.objects.all()
            self.assertTrue(len(images) >= 1)

    def test_delete_method(self):
            self.post=Post(image_name='cat',description='beautiful',user=self.user1,show="image")
            self.post.save_post()
            images = self.post.delete_post
            deleted = Post.objects.all()
            self.assertTrue(len(deleted) <= 0)