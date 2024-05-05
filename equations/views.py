from django.shortcuts import render
import sympy as sp
from . import metodos

# Create your views here.
def busquedas_incrementales_view(request):
    if request.method == 'POST':
        funcion_str = request.POST.get('funcion')
        a = float(request.POST.get('a'))
        b = float(request.POST.get('b'))
        dx = float(request.POST.get('dx'))
        tol = float(request.POST.get('tol'))
        max_iter = int(request.POST.get('max_iter'))
        
        funcion_sympy = sp.sympify(funcion_str)        

        return render(request, 'equations/busquedas_incrementales.html', {'funcion': funcion_sympy})
    else:
        return render(request, 'equations/busquedas_incrementales.html')

def biseccion_view(request):
    if request.method == 'POST':
        funcion_str = request.POST.get('funcion')
        a = float(request.POST.get('a'))
        b = float(request.POST.get('b'))
        tol = float(request.POST.get('tol'))
        max_iter = int(request.POST.get('max_iter'))
        
        funcion_sympy = sp.sympify(funcion_str)        

        return render(request, 'equations/biseccion.html', {'funcion': funcion_sympy})
    else:
        return render(request, 'equations/biseccion.html')
        
def regla_falsa_view(request):
    if request.method == 'POST':
        funcion_str = request.POST.get('funcion')
        a = float(request.POST.get('a'))
        b = float(request.POST.get('b'))
        tol = float(request.POST.get('tol'))
        max_iter = int(request.POST.get('max_iter'))
        
        funcion_sympy = sp.sympify(funcion_str)        
    
        tabla, grafica = metodos.regla_falsa(funcion_sympy, a, b, tol, max_iter)

        return render(request, 'equations/regla_falsa.html', {'tabla': tabla, 'funcion': funcion_sympy, 'grafica': grafica})
    else:
        return render(request, 'equations/regla_falsa.html')

def punto_fijo_view(request):
    if request.method == 'POST':
        funcion_f_str = request.POST.get('funcion_f')
        funcion_g_str = request.POST.get('funcion_g')
        x0 = float(request.POST.get('x0'))
        tol = float(request.POST.get('tol'))
        max_iter = int(request.POST.get('max_iter'))
        
        funcion_f_sympy = sp.sympify(funcion_f_str)  
        funcion_g_sympy = sp.sympify(funcion_g_str)        
        
        return render(request, 'equations/punto_fijo.html', {'funcion_f': funcion_f_sympy, 'funcion_g': funcion_g_sympy})
    else:
        return render(request, 'equations/punto_fijo.html')

def newton_view(request):
    if request.method == 'POST':
        funcion_str = request.POST.get('funcion')
        x0 = float(request.POST.get('x0'))
        tol = float(request.POST.get('tol'))
        max_iter = int(request.POST.get('max_iter'))
        
        x=sp.symbols('x')
        funcion_sympy = sp.sympify(funcion_str)  
        derivada_sympy = sp.diff(funcion_sympy,x)       
        
        return render(request, 'equations/newton.html', {'funcion': funcion_sympy})
    else:
        return render(request, 'equations/newton.html')

def secante_view(request):
    if request.method == 'POST':
        funcion_str = request.POST.get('funcion')
        x0 = float(request.POST.get('x0'))
        x1 = float(request.POST.get('x1'))
        tol = float(request.POST.get('tol'))
        max_iter = int(request.POST.get('max_iter'))

        funcion_sympy = sp.sympify(funcion_str) 

        return render(request, 'equations/secante.html', {'funcion': funcion_sympy})
    else:
        return render(request, 'equations/secante.html')

def raices_multiples_view(request):
    if request.method == 'POST':
        funcion_str = request.POST.get('funcion')
        x0 = float(request.POST.get('x0'))
        tol = float(request.POST.get('tol'))
        max_iter = int(request.POST.get('max_iter'))
        
        x=sp.symbols('x')
        funcion_sympy = sp.sympify(funcion_str)  
        derivada_sympy = sp.diff(funcion_sympy,x)       
        
        return render(request, 'equations/raices_multiples.html', {'funcion': funcion_sympy})
    else:
        return render(request, 'equations/raices_multiples.html')