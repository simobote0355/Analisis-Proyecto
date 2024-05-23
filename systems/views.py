from django.shortcuts import render
import random
import numpy as np
from . import metodos
from django.shortcuts import render

# Create your views here.
def jacobi_view(request):
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        tol = float(request.POST.get('tol'))
        max_iter = int(request.POST.get('max_iter'))
        norma = int(request.POST.get('norma'))
        matriz = np.random.randint(1, 100, size=(n, n))
        b = np.random.randint(1, 100, size=n)
        x0 = np.array([0,0,0])

        print(matriz)
        print(b)
        print(x0)
        tabla, mensaje = metodos.jacobi(matriz, b, x0, tol, max_iter, norma)
        return render(request, 'systems/jacobi.html', {'matriz': matriz, 'b': b, 'x0': x0, 'tabla': tabla.to_html(), 'mensaje': mensaje})
    else:
        return render(request, 'systems/jacobi.html')

def gauss_seidel_view(request):
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        matriz = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
        b = [random.randint(1, 100) for _ in range(n)]
        return render(request, 'systems/gauss_seidel.html', {'matriz': matriz, 'b': b})
    else:
        return render(request, 'systems/gauss_seidel.html')

def sor_view(request):
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        matriz = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
        b = [random.randint(1, 100) for _ in range(n)]
        return render(request, 'systems/sor.html', {'matriz': matriz, 'b': b})
    else:
        return render(request, 'systems/sor.html')
    