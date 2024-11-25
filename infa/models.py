from django.db import models

# step1 create your own user model that subclasses
# django.contrib.auth.models.AbstratUser
# define your own attributes

from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class User(AbstractUser):

    phone=models.CharField(max_length=12)


class UserProfile(models.Model):

    owner=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    bio=models.CharField(max_length=200,null=True)
    profile_picture=models.ImageField(upload_to="images",null=True,blank=True)


class Post(models.Model):

    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    caption=models.CharField(max_length=200,null=True)
    picture=models.ImageField(upload_to="postimage",null=True,blank=True)
    liked_by=models.ManyToManyField(User,related_name="likes")
    created_date=models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.caption


class Comment(models.Model):

    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    post_object=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    message=models.CharField(max_length=200,null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    sticker=models.ImageField(upload_to="sticker",null=True,blank=True)

    def __str__(self) -> str:
        return self.message


def create_profile(sender,instance,created,**kwargs):

    if created:
        UserProfile.objects.create(owner=instance)

post_save.connect(sender=User,receiver=create_profile)
