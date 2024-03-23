from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Video(models.Model):
    name=models.CharField(max_length=100, blank=True)
    image=models.ImageField(blank=True)
    time=models.DateTimeField(auto_now_add=True)
    media=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

class Catigore(models.Model):
    name=models.CharField(max_length=100, blank=True)
    catigore=models.ForeignKey(Video, on_delete=models.CASCADE, related_name='catigores')

class Like(models.Model):
    number=models.IntegerField(default=0)
    owner=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    like=models.ForeignKey(Video, on_delete=models.CASCADE, related_name='likes')

class VideoCommet(models.Model):
    message=models.TextField(blank=True)
    owner=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    commet=models.ForeignKey(Video, on_delete=models.CASCADE, related_name='commets')

class Views(models.Model):
    number=models.IntegerField(default=0)
    view=models.ForeignKey(Video, on_delete=models.CASCADE, related_name='views')

class replyedCommet(models.Model):
    message=models.TextField(blank=True)
    owner=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    replyed=models.ForeignKey(VideoCommet, on_delete=models.CASCADE, related_name='replyeds')

class CommetLike(models.Model):
    number=models.IntegerField(default=0)
    owner=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    like=models.ForeignKey(VideoCommet, on_delete=models.CASCADE, related_name='likes')


    
    
    
    

