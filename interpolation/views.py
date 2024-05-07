from django.shortcuts import render 
from . import metodos

# Create your views here.
def vandermonde_view(request):
    if request.method == 'POST':
        puntos = {"x": [], "y": []}
        punto_str = request.POST.get('punto')
        lista=(punto_str.split(' '))
        for element in lista:
            punto=eval(element)
            x,y=punto
            puntos["x"].append(x)
            puntos["y"].append(y)

        coordenadas=zip(puntos["x"], puntos["y"])   
        return render(request, 'interpolation/vandermonde.html', {'coordenadas': coordenadas})
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
            puntos["x"].append(x)
            puntos["y"].append(y)

        coordenadas=zip(puntos["x"], puntos["y"])   
        return render(request, 'interpolation/newton_inter.html', {'coordenadas': coordenadas})
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
            puntos["x"].append(x)
            puntos["y"].append(y)

        coordenadas=zip(puntos["x"], puntos["y"])   
        return render(request, 'interpolation/lagrange.html', {'coordenadas': coordenadas})
    else:
        return render(request, 'interpolation/lagrange.html')