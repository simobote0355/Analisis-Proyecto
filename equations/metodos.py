import sympy as sp
from sympy import sin, cos, log
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64

def busquedas_incrementales(f, a, b, dx, tol, iter):
    return

def biseccion(f, a, b, tol, iter):
    return

def regla_falsa(f, a, b, Tol, iter):
    # Inicializar variables
    n = 0
    sym_x=sp.symbols('x')
    f = f.subs({'sin': sin, 'cos': cos, 'log': log})
    fa = f.subs(sym_x,a)
    fb = f.subs(sym_x,b)
    E = abs(b - a)
    tabla = [[n, a, fa, E]]

    x_values = np.linspace(1, 20, 1000)  # Utilizamos el rango [a, b]
    y_values = [f.subs(sym_x, x_val) for x_val in x_values]
    plt.plot(x_values, y_values, label='f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico de la función')
    plt.grid(True)
    plt.legend() 
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    grafica = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.close()

    print('%-3s %-20s %-20s %-20s' % ('n', 'xn', 'f(xn)', 'E'))
    print('%-3d %-20.13f %-20.13f %-20.13f' % tuple(tabla[0]))
    
    while E > Tol and n < iter and fa != 0 and fb != 0:
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
    
    return tabla, grafica

def punto_fijo(f, g, x0, tol, iter):
    return

def newton(f, x0, tol, iter):
    return

def secante(f, x0, x1, tol, iter):
    return 

def raices_multiples(f, x0, tol, iter):
    return