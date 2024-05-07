from django.shortcuts import render
import random
from . import metodos

# Create your views here.
def gauss_simple_view(request):
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        matriz = [[random.uniform(1.0, 100.0) for _ in range(n)] for _ in range(n)]
        b = [random.uniform(1.0, 100.0) for _ in range(n)]
        return render(request, 'systems/gauss_simple.html', {'matriz': matriz, 'b': b})
    else:
        return render(request, 'systems/gauss_simple.html')

def gauss_parcial_view(request):
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        matriz = [[random.uniform(1.0, 100.0) for _ in range(n)] for _ in range(n)]
        b = [random.uniform(1.0, 100.0) for _ in range(n)]
        return render(request, 'systems/gauss_parcial.html', {'matriz': matriz, 'b': b})
    else:
        return render(request, 'systems/gauss_parcial.html')

def gauss_total_view(request):
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        matriz = [[random.uniform(1.0, 100.0) for _ in range(n)] for _ in range(n)]
        b = [random.uniform(1.0, 100.0) for _ in range(n)]
        return render(request, 'systems/gauss_total.html', {'matriz': matriz, 'b': b})
    else:
        return render(request, 'systems/gauss_total.html')
    
def lu_simple_view(request):
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        matriz = [[random.uniform(1.0, 100.0) for _ in range(n)] for _ in range(n)]
        b = [random.uniform(1.0, 100.0) for _ in range(n)]
        return render(request, 'systems/lu_simple.html', {'matriz': matriz, 'b': b})
    else:
        return render(request, 'systems/lu_simple.html')

def lu_parcial_view(request):
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        matriz = [[random.uniform(1.0, 100.0) for _ in range(n)] for _ in range(n)]
        b = [random.uniform(1.0, 100.0) for _ in range(n)]
        return render(request, 'systems/lu_parcial.html', {'matriz': matriz, 'b': b})
    else:
        return render(request, 'systems/lu_parcial.html')
