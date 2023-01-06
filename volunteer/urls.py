from django.urls import path
from . import views
urlpatterns = [
    path('volunteer/', views.volunteer, name='volunteer'),
    path('volunteerdetail/', views.volunteerdetail, name='volunteerdetail'),
    path('becomevolunteer', views.becomevolunteer, name='becomevolunteer'),
]