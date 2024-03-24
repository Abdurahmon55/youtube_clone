from rest_framework.serializers import ModelSerializer
from .models import *
from django.contrib.auth import get_user_model

class AuthSerializer(ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=['username', 'id']

def serializer(name, models):
    class name(ModelSerializer):
        class Meta:
            model=models
            fields='__all__'
    return name 

CommetLikeSeializer=serializer('CommetLikeSeializer', CommetLike)
replyedCommetSerializer=serializer('replyedCommetSerializer', replyedCommet)
ViewsSerializer=serializer('ViewsSerializer', Views)
LikeSerializer=serializer('LikeSerializer', Like)
CatigoreSerializer=serializer('CatigoreSerializer', Catigore)



class VideoCommetSerializer(ModelSerializer):
    replyeds=replyedCommetSerializer(many=True, read_only = True)
    likes=CommetLikeSeializer(many=True, read_only = True)
    class Meta:
        model=VideoCommet
        fields='__all__'

class VideoSerializer(ModelSerializer):
    catigores=CatigoreSerializer(many=True, read_only = True)
    likes=LikeSerializer(many=True, read_only = True)
    commets=VideoCommetSerializer(many=True, read_only = True)
    views=ViewsSerializer(many=True, read_only = True)
    class Meta:
        model=Video
        fields='__all__'

