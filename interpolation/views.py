from django.shortcuts import render

# Create your views here.
def vandermonde(request):
    return render(request, 'interpolation/vandermonde.html')

def newton_inter(request):
    return render(request, 'interpolation/newton_inter.html')

def lagrange(request):
    return render(request, 'interpolation/lagrange.html')
