from django.urls import path
from . import views

urlpatterns = [
    path('vandermonde/', views.vandermonde, name='vandermonde'),
    path('newton_inter/', views.newton_inter, name='newton_inter'),
    path('lagrange/', views.lagrange, name='lagrange'),
   
]