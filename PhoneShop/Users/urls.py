from django.urls import path
from .views import registration_user, login_user, logout_user
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('registration', registration_user, name='registration'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
] 
