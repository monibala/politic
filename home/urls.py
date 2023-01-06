from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.events, name='events'),
    path('eventdetail/', views.eventdetail, name='eventdetail'),
    path('gallery/', views.gallery, name='gallery'),
    path('history/', views.history, name='history'),
    path('donate/', views.donate, name='donate'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
]