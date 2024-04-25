from django.urls import path
from . import views

urlpatterns = [
    path('busquedas_incrementales/', views.busquedas_incrementales, name='busquedas_incrementales'),
    path('biseccion/', views.biseccion, name='biseccion'),
    path('regla_falsa/', views.regla_falsa, name='regla_falsa'),
    path('punto_fijo/', views.punto_fijo, name='punto_fijo'),
    path('newton/', views.newton, name='newton'),
    path('secante/', views.secante, name='secante'),
    path('raices_multiples/', views.raices_multiples, name='raices_multiples'),
]