from django.shortcuts import render
import sympy as sp
from sympy import sin, cos, log

# Create your views here.

def busquedas_incrementales_view(request):
    return render(request, 'equations/busquedas_incrementales.html')

def biseccion_view(request):
    return render(request, 'equations/biseccion.html')

def regla_falsa(f, a, b, Tol, maxIter):
    # Inicializar variables
    n = 0
    function=sp.sympify(f)
    sym_x=sp.symbols('x')
    function = function.subs({'sin': sin, 'cos': cos, 'log': log})
    fa = function.subs(sym_x,a)
    fb = function.subs(sym_x,b)
    E = abs(b - a)
    tabla = [[n, a, fa, E]]
    print('%-3s %-20s %-20s %-20s' % ('n', 'xn', 'f(xn)', 'E'))
    print('%-3d %-20.13f %-20.13f %-20.13f' % tuple(tabla[0]))
    
    while E > Tol and n < maxIter and fa != 0 and fb != 0:
        # Calcular nuevo punto
        xn = a - fa*(b - a)/(fb - fa)
        fxn = function.subs(sym_x,xn)
        
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
    
    return tabla


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
        
        # Llamamos a la función de la regla falsa y obtenemos la tabla de resultados
        tabla = regla_falsa(funcion, a, b, tol, max_iter)
        
        # Renderizamos la tabla de resultados en la plantilla y la devolvemos
        return render(request, 'equations/regla_falsa.html', {'tabla': tabla})
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