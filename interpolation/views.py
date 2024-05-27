from django.shortcuts import render 
from . import metodos
import json

# Create your views here.
def vandermonde_view(request):
    if request.method == 'POST':
        puntos = {"x": [], "y": []}
        punto_str = request.POST.get('punto')
        lista=(punto_str.split(' '))
        for element in lista:
            punto=eval(element)
            x,y=punto
            x=float(x)
            y=float(y)
            puntos["x"].append(x)
            puntos["y"].append(y)

        coordenadas=zip(puntos["x"], puntos["y"])   
        resultado=metodos.vandermonde(puntos)

        with open('interpolation/registros.txt', 'a') as file:
            file.write("Vandermonde")
            file.write('\n\n')    
            file.write(json.dumps(puntos))
            file.write('\n\n')
            file.write(str(resultado)) 
            file.write('\n\n\n')

        return render(request, 'interpolation/vandermonde.html', {'coordenadas': coordenadas, 'resultado': resultado})
    else:
        return render(request, 'interpolation/vandermonde.html')
    
def newton_inter_view(request):
    if request.method == 'POST':
        puntos = {"x": [], "y": []}
        punto_str = request.POST.get('punto')
        lista=(punto_str.split(' '))
        for element in lista:
            punto=eval(element)
            x,y=punto
            x=float(x)
            y=float(y)
            puntos["x"].append(x)
            puntos["y"].append(y)

        coordenadas=zip(puntos["x"], puntos["y"])   
        tabla, pol=metodos.newton_inter(puntos)

        with open('interpolation/registros.txt', 'a') as file:
            file.write("Newton")
            file.write('\n\n')    
            file.write(json.dumps(puntos))
            file.write('\n\n')
            file.write(str(pol)) 
            file.write('\n\n\n')

        return render(request, 'interpolation/newton_inter.html', {'coordenadas': coordenadas, 'tabla': tabla.to_html(), 'pol': pol})
    else:
        return render(request, 'interpolation/newton_inter.html')

def lagrange_view(request):
    if request.method == 'POST':
        puntos = {"x": [], "y": []}
        punto_str = request.POST.get('punto')
        lista=(punto_str.split(' '))
        for element in lista:
            punto=eval(element)
            x,y=punto
            x=float(x)
            y=float(y)
            puntos["x"].append(x)
            puntos["y"].append(y)

        coordenadas=zip(puntos["x"], puntos["y"])
        pol=metodos.lagrange(puntos)

        with open('interpolation/registros.txt', 'a') as file:
            file.write("Lagrange")
            file.write('\n\n')    
            file.write(json.dumps(puntos))
            file.write('\n\n')
            file.write(str(pol)) 
            file.write('\n\n\n')

        return render(request, 'interpolation/lagrange.html', {'coordenadas': coordenadas, 'pol': pol})
    else:
        return render(request, 'interpolation/lagrange.html')
    
def spline_view(request):
    if request.method == 'POST':
        puntos = {"x": [], "y": []}
        punto_str = request.POST.get('punto')
        grado= int(request.POST.get('grado'))
        lista=(punto_str.split(' '))
        for element in lista:
            punto=eval(element)
            x,y=punto
            x=float(x)
            y=float(y)
            puntos["x"].append(x)
            puntos["y"].append(y)

        coordenadas=zip(puntos["x"], puntos["y"]) 
        pols, intervalos =metodos.spline(puntos, grado) 
        datos=zip(pols,intervalos)

        with open('interpolation/registros.txt', 'a') as file:
            file.write("Vandermonde")
            file.write('\n\n')    
            file.write(json.dumps(puntos))
            file.write('\n\n')
            for pol in pols:
                file.write(str(pol)) 
                file.write('\n\n')

        return render(request, 'interpolation/spline.html', {'coordenadas': coordenadas, 'datos': datos})
    else:
        return render(request, 'interpolation/spline.html')