from django.shortcuts import render
import sympy as sp
from sympy import sin, cos, log
import matplotlib.pyplot as plt
import numpy as np
import tempfile
import os

# Create your views here.

def busquedas_incrementales_view(request):
    return render(request, 'equations/busquedas_incrementales.html')

def biseccion_view(request):
    return render(request, 'equations/biseccion.html')

def regla_falsa(f, a, b, Tol, maxIter):
    # Inicializar variables
    n = 0
    sym_x=sp.symbols('x')
    f = f.subs({'sin': sin, 'cos': cos, 'log': log})
    fa = f.subs(sym_x,a)
    fb = f.subs(sym_x,b)
    E = abs(b - a)
    tabla = [[n, a, fa, E]]

    x_values = np.linspace(a, b, 1000)
    y_values = [f.subs(sym_x, x_val) for x_val in x_values]
    plt.plot(x_values, y_values, label='f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico de la función')
    plt.grid(True)
    plt.legend() 
    _, plot_path = tempfile.mkstemp('.png')
    plt.savefig(plot_path)
    plt.close()

    print('%-3s %-20s %-20s %-20s' % ('n', 'xn', 'f(xn)', 'E'))
    print('%-3d %-20.13f %-20.13f %-20.13f' % tuple(tabla[0]))
    
    while E > Tol and n < maxIter and fa != 0 and fb != 0:
        # Calcular nuevo punto
        xn = a - fa*(b - a)/(fb - fa)
        fxn = f.subs(sym_x,xn)
        
        # Actualizar intervalo
        if fa * fxn < 0:
            b = xn
            fb = fxn
        else:
            a = xn
            fa = fxn
        
        # Calcular error absoluto
        E = abs(b - a)
        
        # Actualizar contador y tabla
        n += 1
        tabla.append([n, xn, fxn, E])
        print('%-3d %-20.13f %-20.13f %-20.13f' % tuple(tabla[-1]))
    
    return tabla, plot_path

def regla_falsa_view(request):
    if request.method == 'POST':
        # Obtenemos la función ingresada por el usuario desde el formulario
        funcion = request.POST.get('funcion')
        # Obtenemos los extremos del intervalo a y b
        a = float(request.POST.get('a'))
        b = float(request.POST.get('b'))
        # Obtenemos la tolerancia y el número máximo de iteraciones
        tol = float(request.POST.get('tol'))
        max_iter = int(request.POST.get('max_iter'))
        funcion_sympy = sp.sympify(funcion)
        funcion_latex = sp.latex(funcion_sympy)

        
        # Llamamos a la función de la regla falsa y obtenemos la tabla de resultados
        tabla, plot_path = regla_falsa(funcion_sympy, a, b, tol, max_iter)
        
        # Renderizamos la tabla de resultados en la plantilla y la devolvemos
        return render(request, 'equations/regla_falsa.html', {'tabla': tabla, 'latex': funcion_latex, 'plot_path': plot_path})
    else:
        return render(request, 'equations/regla_falsa.html')

def punto_fijo_view(request):
    return render(request, 'equations/punto_fijo.html')

def newton_view(request):
    return render(request, 'equations/newton.html')

def secante_view(request):
    return render(request, 'equations/secante.html')

def raices_multiples_view(request):
    return render(request, 'equations/raices_multiples.html')