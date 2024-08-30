from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('accueil/',views.accueil,name='accueil'),
    path('login/',views.LoginF,name="login"),
    path('register/',views.RegisterF,name="register"),
    path('Logout/',views.logout_view,name="logout"),
    path('promptchat/',views.promptchat,name="promptchat")
]