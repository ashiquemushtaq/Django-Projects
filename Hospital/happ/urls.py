from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about-us',views.about,name="about"),
    path('appointment',views.appointment,name="appointment"),
    path('doctors',views.doctors,name="doctors"),
    path('departments/<slug:dep_slug>',views.departments,name="departments"),
]