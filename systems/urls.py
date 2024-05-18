from django.urls import path
from . import views

urlpatterns = [
    path('gauss_simple/', views.gauss_simple_view, name='gauss_simple'),
    path('gauss_parcial/', views.gauss_parcial_view, name='gauss_parcial'),
    path('gauss_total/', views.gauss_total_view, name='gauss_total'),
    path('lu_simple/', views.lu_simple_view, name='lu_simple'),
    path('lu_parcial/', views.lu_parcial_view, name='lu_parcial'),
    path('croult/', views.croult_view, name='croult'),
    path('doolittle/', views.doolittle_view, name='doolittle'),
    path('cholesky/', views.cholesky_view, name='cholesky'),
    path('iterativos/', views.iterativos_view, name='iterativos'),
]