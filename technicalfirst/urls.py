from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('privacy/', views.privacy, name='privacy'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('post/<str:post_slug>', views.post, name='post'),
    # Subscriber Api
    path('subscribers/', views.subscribers, name='subscribers'),
]