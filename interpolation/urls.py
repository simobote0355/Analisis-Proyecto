from django.urls import path
from . import views

urlpatterns = [
    path('vandermonde/', views.vandermonde_view, name='vandermonde'),
    path('newton_inter/', views.newton_inter_view, name='newton_inter'),
    path('lagrange/', views.lagrange_view, name='lagrange'),
   
]