from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('tweet/create/', views.CreateTweet.as_view()),
    path('tweets/list/', views.TweetsList.as_view()),
    path('tweet/<int:pk>/detail/', views.TweetDetail.as_view()),
    path('tweet/<int:pk>/delete/', views.DeleteTweet.as_view()),
    path('tweet/<int:pk>/update/', views.UpdateTweet.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
