from django.urls import path
from . import views

urlpatterns = [
    path('ej/', views.index, name='index'),
    path('process_matrix/<int:n>', views.process_matrix, name='process_matrix')
]