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
        
        datos={"Función": funcion_str, "(a,b)": (a,b), "dx": dx, "tol": tol, "iter": max_iter}              

        return render(request, 'equations/busquedas_incrementales.html', {'datos':  datos})
    else:
        return render(request, 'equations/busquedas_incrementales.html')

def biseccion_view(request):
    if request.method == 'POST':
        funcion_str = request.POST.get('funcion')
        a = float(request.POST.get('a'))
        b = float(request.POST.get('b'))
        tol = float(request.POST.get('tol'))
        max_iter = int(request.POST.get('max_iter'))
        
        datos={"Función": funcion_str, "(a,b)": (a,b), "tol": tol, "iter": max_iter}
        tabla, mensaje = metodos.biseccion(funcion_str, a, b, tol, max_iter)      

        return render(request, 'equations/biseccion.html', {"datos": datos, 'tabla': tabla.to_html(), 'mensaje': mensaje})
    else:
        return render(request, 'equations/biseccion.html')
        
def regla_falsa_view(request):
    if request.method == 'POST':
        funcion_str = request.POST.get('funcion')
        a = float(request.POST.get('a'))
        b = float(request.POST.get('b'))
        tol = float(request.POST.get('tol'))
        max_iter = int(request.POST.get('max_iter'))
        
        datos={"Función": funcion_str, "(a,b)": (a,b), "tol": tol, "iter": max_iter}

        return render(request, 'equations/regla_falsa.html', {'datos': datos})
    else:
        return render(request, 'equations/regla_falsa.html')

def punto_fijo_view(request):
    if request.method == 'POST':
        funcion_f_str = request.POST.get('funcion_f')
        funcion_g_str = request.POST.get('funcion_g')
        x0 = float(request.POST.get('x0'))
        tol = float(request.POST.get('tol'))
        max_iter = int(request.POST.get('max_iter'))
        
        datos={"Función f(x)": funcion_f_str, "Función g(x)": funcion_g_str, "x0": x0, "tol": tol, "iter": max_iter} 
        tabla, mensaje = metodos.punto_fijo(funcion_f_str,funcion_g_str, x0, tol, max_iter)
    
        return render(request, 'equations/punto_fijo.html', {'datos': datos, 'tabla': tabla.to_html(), 'mensaje': mensaje})
    else:
        return render(request, 'equations/punto_fijo.html')

def newton_view(request):
    if request.method == 'POST':
        funcion_str = request.POST.get('funcion')
        x0 = float(request.POST.get('x0'))
        tol = float(request.POST.get('tol'))
        max_iter = int(request.POST.get('max_iter'))
        
        datos={"Función": funcion_str, "x0": x0, "tol": tol, "iter": max_iter}
        tabla, mensaje = metodos.newton(funcion_str, x0, tol, max_iter)
        return render(request, 'equations/newton.html', {'datos': datos, 'tabla': tabla.to_html(), 'mensaje': mensaje})
    else:
        return render(request, 'equations/newton.html')

def secante_view(request):
    if request.method == 'POST':
        funcion_str = request.POST.get('funcion')
        x0 = float(request.POST.get('x0'))
        x1 = float(request.POST.get('x1'))
        tol = float(request.POST.get('tol'))
        max_iter = int(request.POST.get('max_iter'))

        datos={"Función": funcion_str, "x0": x0, "x1": x1, "tol": tol, "iter": max_iter} 
        tabla, mensaje = metodos.newton(funcion_str, x0, tol, max_iter)
        return render(request, 'equations/secante.html', {'funcion': datos, 'tabla': tabla.to_html(), 'mensaje': mensaje})
    else:
        return render(request, 'equations/secante.html')

def raices_multiples_view(request):
    if request.method == 'POST':
        funcion_str = request.POST.get('funcion')
        x0 = float(request.POST.get('x0'))
        tol = float(request.POST.get('tol'))
        max_iter = int(request.POST.get('max_iter'))
        
        datos={"Función": funcion_str, "x0": x0, "tol": tol, "iter": max_iter}      
        
        return render(request, 'equations/raices_multiples.html', {'datos': datos})
    else:
        return render(request, 'equations/raices_multiples.html')