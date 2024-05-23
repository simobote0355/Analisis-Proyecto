from django.urls import path
from . import views

urlpatterns = [
    path('jacobi/', views.doolittle_view, name='jacobi'),
    path('gauss_seidel/', views.cholesky_view, name='gauss_seidel'),
    path('sor/', views.iterativos_view, name='sor'),
]