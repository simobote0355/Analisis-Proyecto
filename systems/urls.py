from django.urls import path
from . import views

urlpatterns = [
    path('gauss_simple/', views.gauss_simple, name='gauss_simple'),
    path('gauss_parcial/', views.gauss_parcial, name='gauss_parcial'),
    path('gauss_total/', views.gauss_total, name='gauss_total'),
    path('lu_simple/', views.lu_simple, name='lu_simple'),
    path('lu_parcial/', views.lu_parcial, name='lu_parcial'),
    path('jacobi/', views.jacobi, name='jacobi'),
    path('sor/', views.sor, name='sor'),
]