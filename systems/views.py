from django.shortcuts import render
import random
import numpy as np
from . import metodos

# Create your views here.
def index(request):
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        rango=range(n)
        return render(request, 'systems/matrix_input.html', {'rango': rango, 'n': n})
    return render(request, 'systems/index.html')

def process_matrix(request,n):
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        method = request.POST.get('method')
        tol = float(request.POST.get('tol'))
        max_iter = int(request.POST.get('max_iter'))
        norma = int(request.POST.get('norma'))
        w = float(request.POST.get('w')) if method == 'sor' else None

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
            
        if method=='jacobi':
            tabla, mensaje, radio = metodos.jacobi(np.array(matrix), np.array(vector1), np.array(vector2), tol, max_iter, norma)
            return render(request, 'systems/jacobi.html', {'matriz': np.array(matrix), 'b': np.array(vector1), 'x0': np.array(vector2), 'tabla': tabla.to_html(), 'mensaje': mensaje, "radio": radio})

        if method=='gauss_seidel':
            tabla, mensaje, radio = metodos.gauss_seidel(np.array(matrix), np.array(vector1), np.array(vector2), tol, max_iter, norma)
            return render(request, 'systems/gauss_seidel.html', {'matriz': matrix, 'b': np.array(vector1), 'x0': np.array(vector2), 'tabla': tabla.to_html(), 'mensaje': mensaje, "radio": radio})

        if method=='sor':
            tabla, mensaje, radio = metodos.sor(np.array(matrix), np.array(vector1), np.array(vector2), tol, max_iter, norma, w)
            return render(request, 'systems/sor.html', {'matriz': np.array(matrix), 'b': np.array(vector1), 'x0': np.array(vector2), 'tabla': tabla.to_html(), 'mensaje': mensaje, "radio": radio})
        #return render(request, 'systems/matrix_result.html', {'matrix': matrix, 'vector1': vector1, 'vector2': vector2})
    return render(request, 'systems/index.html')
