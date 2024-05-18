from django.shortcuts import render
import random
from . import metodos

# Create your views here.
def gauss_simple_view(request):
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        matriz = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
        b = [random.randint(1, 100) for _ in range(n)]
        return render(request, 'systems/gauss_simple.html', {'matriz': matriz, 'b': b})
    else:
        return render(request, 'systems/gauss_simple.html')

def gauss_parcial_view(request):
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        matriz = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
        b = [random.randint(1, 100) for _ in range(n)]
        return render(request, 'systems/gauss_parcial.html', {'matriz': matriz, 'b': b})
    else:
        return render(request, 'systems/gauss_parcial.html')

def gauss_total_view(request):
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        matriz = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
        b = [random.randint(1, 100) for _ in range(n)]
        return render(request, 'systems/gauss_total.html', {'matriz': matriz, 'b': b})
    else:
        return render(request, 'systems/gauss_total.html')
    
def lu_simple_view(request):
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        matriz = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
        b = [random.randint(1, 100) for _ in range(n)]
        return render(request, 'systems/lu_simple.html', {'matriz': matriz, 'b': b})
    else:
        return render(request, 'systems/lu_simple.html')

def lu_parcial_view(request):
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        matriz = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
        b = [random.randint(1, 100) for _ in range(n)]
        return render(request, 'systems/lu_parcial.html', {'matriz': matriz, 'b': b})
    else:
        return render(request, 'systems/lu_parcial.html')

def croult_view(request):
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        matriz = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
        b = [random.randint(1, 100) for _ in range(n)]
        return render(request, 'systems/croult.html', {'matriz': matriz, 'b': b})
    else:
        return render(request, 'systems/croult.html')
    
def doolittle_view(request):
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        matriz = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
        b = [random.randint(1, 100) for _ in range(n)]
        return render(request, 'systems/doolittle.html', {'matriz': matriz, 'b': b})
    else:
        return render(request, 'systems/doolittle.html')
    
def cholesky_view(request):
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        matriz = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
        b = [random.randint(1, 100) for _ in range(n)]
        return render(request, 'systems/cholesky.html', {'matriz': matriz, 'b': b})
    else:
        return render(request, 'systems/cholesky.html')
    
def iterativos_view(request):
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        metodo = int(request.POST.get('metodo'))
        matriz = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
        b = [random.randint(1, 100) for _ in range(n)]
        return render(request, 'systems/iterativos.html', {'matriz': matriz, 'b': b, 'metodo': metodo})
    else:
        return render(request, 'systems/iterativos.html')