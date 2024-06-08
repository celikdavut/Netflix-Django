from django.urls import path

from .views import *

urlpatterns = [
    path("login/",userLogin,name="login"),
    path("browse/",profiles,name="browse"),
    path('register/',register,name="register"),
    path('create-profil/',createProfile,name="create-profil"),
    path('account/',userAccount,name="user-account"),
    path('remove/',removeAccount,name="remove")
]
