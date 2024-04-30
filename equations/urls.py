from django.urls import path
from . import views

urlpatterns = [
    path('busquedas_incrementales/', views.busquedas_incrementales_view, name='busquedas_incrementales'),
    path('biseccion/', views.biseccion_view, name='biseccion'),
    path('regla_falsa/', views.regla_falsa_view, name='regla_falsa'),
    path('punto_fijo/', views.punto_fijo_view, name='punto_fijo'),
    path('newton/', views.newton_view, name='newton'),
    path('secante/', views.secante_view, name='secante'),
    path('raices_multiples/', views.raices_multiples_view, name='raices_multiples'),
]