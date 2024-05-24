from django.shortcuts import render
import random
import numpy as np
from . import metodos

# Create your views here.
def jacobi_view(request):
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        tol = int(request.POST.get('tol'))
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
    
from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        rango=range(n)
        return render(request, 'systems/matrix_input.html', {'rango': rango, 'n': n})
    return render(request, 'systems/index.html')

def process_matrix(request,n):
    n = int(request.POST.get('n'))
    method = request.POST.get('method')
    if request.method == 'POST':
        
        matrix = []
        vector1 = []
        vector2 = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(int(request.POST.get(f'matrix_{i}_{j}')))
            matrix.append(row)
            vector1.append(int(request.POST.get(f'vector1_{i}')))
            vector2.append(int(request.POST.get(f'vector2_{i}')))

        print(matrix)
        print(vector1)
        print(vector2)
        if method=='jacobi':
            print("holaaaa")
            tabla, mensaje = metodos.jacobi(np.array(matrix), np.array(vector1), np.array(vector2), 5e-5, 100, 2)
            return render(request, 'systems/jacobi.html', {'matriz': matrix, 'b': vector1, 'x0': vector2, 'tabla': tabla.to_html(), 'mensaje': mensaje})

        #return render(request, 'systems/matrix_result.html', {'matrix': matrix, 'vector1': vector1, 'vector2': vector2})
    return render(request, 'systems/index.html')
