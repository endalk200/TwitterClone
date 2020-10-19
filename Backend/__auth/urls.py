from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

from knox.views import LogoutView

urlpatterns = [
    # custom CreateUser view
    path('user/create/', views.CreateUser.as_view()),
    path('user/login/', views.UserLogin.as_view()),

    # since Logout Views are implemented in knox LogoutView
    path('user/logout/', LogoutView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
