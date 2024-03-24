from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns=[
    path('profil/', AuthViews.as_view()),
    path('video/', VideoViews.as_view()),
    path('video/<int:pk>/', VideoDetailViews.as_view()),
    path('video/catigore/', CatigoreViews.as_view()),
    path('video/catigore/<int:pk>/', CatigoreDetailViews.as_view()),
    path('video/like/', LikeViews.as_view()),
    path('video/like/<int:pk>/', LikeDetailViews.as_view()),
    path('video/views/<int:pk>/', ViewsDetailViews.as_view()),
    path('video/views/', ViewsViews.as_view()),
    path('video/commet/', VideoCommetViews.as_view()),
    path('video/commet/<int:pk>/', VideoCommetDetailViews.as_view()),
    path('video/commet/replyed/', replyedCommetViews.as_view()),
    path('video/commet/replyed/<int:pk>/', replyedCommetDetailViews.as_view()),
    path('video/commet/like/', CommetLikeViews.as_view()),
    path('video/commet/like/<int:pk>/', CommetLikeDetailViews.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]