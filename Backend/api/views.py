from django.shortcuts import render
from rest_framework.generics import *
from .serializers import *
from .models import *
from django.contrib.auth import get_user_model
# Create your views here.

def View(name, views, model, serializer):
    class name(views):
        queryset=model.objects.all()
        serializer_class=serializer
    return name

AuthViews=View('AuthViews', ListAPIView, get_user_model(), AuthSerializer)
VideoViews=View('VideoViews', ListCreateAPIView, Video, VideoSerializer)
VideoDetailViews=View('VideoDetailViews', RetrieveDestroyAPIView, Video, VideoSerializer)
CatigoreViews=View('CatigoreViews', ListCreateAPIView, Catigore, CatigoreSerializer)
CatigoreDetailViews=View('CatigoreDetailViews', RetrieveDestroyAPIView, Catigore, CatigoreSerializer)
LikeViews=View('LikeViews', ListCreateAPIView, Like, LikeSerializer)
LikeDetailViews=View('LikeDetailViews', RetrieveDestroyAPIView, Like, LikeSerializer)
VideoCommetViews=View('VideoCommetViews', ListCreateAPIView, VideoCommet, VideoCommetSerializer)
VideoCommetDetailViews=View('VideoCommetDetailViews', ListCreateAPIView, VideoCommet, VideoCommetSerializer)
ViewsViews=View('ViewsViews', ListCreateAPIView, Views, ViewsSerializer)
ViewsDetailViews=View('ViewsDetailViews', RetrieveDestroyAPIView, Views, ViewsSerializer)
replyedCommetViews=View('replyedCommetViews', ListCreateAPIView, replyedCommet, replyedCommetSerializer)
replyedCommetDetailViews=View('replyedCommetDetailViews', RetrieveDestroyAPIView, replyedCommet, replyedCommetSerializer)
CommetLikeViews=View('CommetLike', ListCreateAPIView, CommetLike, CommetLikeSeializer)
CommetLikeDetailViews=View('CommetLikeDetailViews', RetrieveDestroyAPIView, CommetLike, CommetLikeSeializer)