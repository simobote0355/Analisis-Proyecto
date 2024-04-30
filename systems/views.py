from django.shortcuts import render

# Create your views here.
def gauss_simple_view(request):
    
    return render(request, 'systems/gauss_simple.html')

def gauss_parcial_view(request):
    return render(request, 'systems/gauss_parcial.html')

def gauss_total_view(request):
    return render(request, 'systems/gauss_total.html')

def lu_simple_view(request):
    return render(request, 'systems/lu_simple.html')

def lu_parcial_view(request):
    return render(request, 'systems/lu_parcial.html')

def jacobi_view(request):
    return render(request, 'systems/jacobi.html')

def sor_view(request):
    return render(request, 'systems/sor.html')