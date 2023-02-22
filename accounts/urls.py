from .views import RegisterAPI
from django.urls import include, path
from .views import RegisterAPI
from .views import LoginAPI
from knox import views as knox_views
from accounts import views

urlpatterns = [
    path('api/register', RegisterAPI.as_view(), name='register'),
    path('api/login', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
