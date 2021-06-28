from django.urls import path
from userlogin import views


urlpatterns = [
    path('register/',views.Register, name='Register'),
    path('login/',views.Login, name='login'),
    path('home/',views.Home, name='home'),
    path('base/',views.base, name='base'),
]