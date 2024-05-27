from django.shortcuts import render
from . import metodos
import json

# Create your views here.
def biseccion_view(request):
    if request.method == 'POST':
        funcion_str = request.POST.get('funcion')
        a = float(request.POST.get('a'))
        b = float(request.POST.get('b'))
        tol = float(request.POST.get('tol'))
        max_iter = int(request.POST.get('max_iter'))
      
        datos={"funcion": funcion_str, "a": a, "b": b, "tol": tol, "max_iter": max_iter}
        tabla, mensaje = metodos.biseccion(funcion_str, a, b, tol, max_iter)   

        with open('equations/registros.txt', 'a') as file:
            file.write("Biseccion")
            file.write('\n\n')  
            file.write(json.dumps(datos))
            file.write('\n\n')
            file.write(tabla.to_string()) 
            file.write('\n\n\n')

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
        
        datos={"funcion": funcion_str, "a": a, "b": b, "tol": tol, "max_iter": max_iter}
        tabla, mensaje = metodos.regla_falsa(funcion_str, a, b, tol, max_iter)

        with open('equations/registros.txt', 'a') as file:
            file.write("Regla Falsa")
            file.write('\n\n')    
            file.write(json.dumps(datos))
            file.write('\n\n')
            file.write(tabla.to_string()) 
            file.write('\n\n\n')

        return render(request, 'equations/regla_falsa.html', {'datos': datos, 'tabla': tabla.to_html(), 'mensaje': mensaje})
    else:
        return render(request, 'equations/regla_falsa.html')

def punto_fijo_view(request):
    if request.method == 'POST':
        funcion_f_str = request.POST.get('funcion_f')
        funcion_g_str = request.POST.get('funcion_g')
        x0 = float(request.POST.get('x0'))
        tol = float(request.POST.get('tol'))
        max_iter = int(request.POST.get('max_iter'))
        
        datos={"funcion_f": funcion_f_str, "funcion_g": funcion_g_str, "x0": x0, "tol": tol, "max_iter": max_iter} 
        tabla, mensaje = metodos.punto_fijo(funcion_f_str,funcion_g_str, x0, tol, max_iter)

        with open('equations/registros.txt', 'a') as file:
            file.write("Punto Fijo")
            file.write('\n\n')    
            file.write(json.dumps(datos))
            file.write('\n\n')
            file.write(tabla.to_string()) 
            file.write('\n\n\n')
    
        return render(request, 'equations/punto_fijo.html', {'datos': datos, 'tabla': tabla.to_html(), 'mensaje': mensaje})
    else:
        return render(request, 'equations/punto_fijo.html')

def newton_view(request):
    if request.method == 'POST':
        funcion_str = request.POST.get('funcion')
        x0 = float(request.POST.get('x0'))
        tol = float(request.POST.get('tol'))
        max_iter = int(request.POST.get('max_iter'))
        
        datos={"funcion": funcion_str, "x0": x0, "tol": tol, "max_iter": max_iter}
        tabla, mensaje = metodos.newton(funcion_str, x0, tol, max_iter)

        with open('equations/registros.txt', 'a') as file:
            file.write("Newton")
            file.write('\n\n')   
            file.write(json.dumps(datos))
            file.write('\n\n')
            file.write(tabla.to_string()) 
            file.write('\n\n\n')

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

        datos={"funcion": funcion_str, "x0": x0, "x1": x1, "tol": tol, "max_iter": max_iter}
        tabla, mensaje = metodos.secante(funcion_str, x0, x1, tol, max_iter)

        with open('equations/registros.txt', 'a') as file:
            file.write("Secante")
            file.write('\n\n')   
            file.write(json.dumps(datos))
            file.write('\n\n')
            file.write(tabla.to_string()) 
            file.write('\n\n\n')

        return render(request, 'equations/secante.html', {'datos': datos, 'tabla': tabla.to_html(), 'mensaje': mensaje})
    else:
        return render(request, 'equations/secante.html')

def raices_multiples_view(request):
    if request.method == 'POST':
        funcion_str = request.POST.get('funcion')
        x0 = float(request.POST.get('x0'))
        tol = float(request.POST.get('tol'))
        max_iter = int(request.POST.get('max_iter'))
        
        datos={"funcion": funcion_str, "x0": x0, "tol": tol, "max_iter": max_iter}  
        tabla, mensaje= metodos.raices_multiples(funcion_str, x0, tol, max_iter)

        with open('equations/registros.txt', 'a') as file:
            file.write("Raices multiples")
            file.write('\n\n')    
            file.write(json.dumps(datos))
            file.write('\n\n')
            file.write(tabla.to_string()) 
            file.write('\n\n\n')    
        
        return render(request, 'equations/raices_multiples.html', {'datos': datos, 'tabla': tabla.to_html(), 'mensaje': mensaje})
    else:
        return render(request, 'equations/raices_multiples.html')