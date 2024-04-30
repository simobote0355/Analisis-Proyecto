from django.shortcuts import render

# Create your views here.
def vandermonde_view(request):
    return render(request, 'interpolation/vandermonde.html')

def newton_inter_view(request):
    return render(request, 'interpolation/newton_inter.html')

def lagrange_view(request):
    return render(request, 'interpolation/lagrange.html')
