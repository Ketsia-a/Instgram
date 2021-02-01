from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, default='No bio')
    profile = models.ImageField(upload_to='profiles/', default='a.png')
    date = models.DateTimeField(auto_now_add=True, null=True)


    @classmethod
    def get_all_instagram_users(cls):
        insta_users = cls.objects.all()

        return insta_users

    def save_profile(self):
        self.save()

    def delete_profile():
        self.delete()

    @classmethod
    def update_user_profile(cls, id, value):
        cls.objects.filter(id = id).update(user_id = new_user)

    @classmethod
    def search_by_profile(cls, username):
        certain_user = cls.objects.filter(user__username__icontains = username)

        return certain_user

    def __str__(self):
        return self.user.username

class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    name = models.CharField(max_length=250, blank=True)
    caption = models.CharField(max_length=250, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null = True,related_name='posts')
    likes = models.ManyToManyField(User, related_name='likes', blank=True, )
    # @classmethod
    # def get_all_images(cls):
    #     images = cls.objects.all().prefetch_related('comments_set')

    #     return images
    class Meta:
        ordering = ["-pk"]

    def total_likes(self):
        return self.likes.count()
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    def get_absolute_url(self):
        return f"/post/{self.id}"

    @classmethod
    def update_caption(cls,id,caption):
        update_image = cls.objects.filter(id = id).update(image_caption = caption)

        return update_image

    def __str__(self):

        return self.name

class Follow(models.Model):
    following = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followers = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return self.following
  

class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True, null=True)
    
    def save_comments(self):
        self.save()

    def delete_comments(self):
        self.delete()

    def update_comment(self):
        self.update()

    def __str__(self):

        return self.posted_by.comment
    

    class Meta:
        ordering = ["-pk"]