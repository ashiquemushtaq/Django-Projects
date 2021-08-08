from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('add',views.add,name="add"),
    path('details/<int:blog_id>',views.details,name="details"),
    path('edit/<int:blog_id>',views.edit,name="edit"),
    path('delete/<int:blog_id>',views.delete,name="delete"),
    path('logout',views.logout,name="logout")
]