from django.shortcuts import render

# Create your views here.
def busquedas_incrementales(request):
    return render(request, 'equations/busquedas_incrementales.html')

def biseccion(request):
    return render(request, 'equations/biseccion.html')

def regla_falsa(request):
    return render(request, 'equations/regla_falsa.html')

def punto_fijo(request):
    return render(request, 'equations/punto_fijo.html')

def newton(request):
    return render(request, 'equations/newton.html')

def secante(request):
    return render(request, 'equations/secante.html')

def raices_multiples(request):
    return render(request, 'equations/raices_multiples.html')