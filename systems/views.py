from django.shortcuts import render

# Create your views here.
def gauss_simple(request):
    return render(request, 'systems/gauss_simple.html')

def gauss_parcial(request):
    return render(request, 'systems/gauss_parcial.html')

def gauss_total(request):
    return render(request, 'systems/gauss_total.html')

def lu_simple(request):
    return render(request, 'systems/lu_simple.html')

def lu_parcial(request):
    return render(request, 'systems/lu_parcial.html')

def jacobi(request):
    return render(request, 'systems/jacobi.html')

def sor(request):
    return render(request, 'systems/sor.html')