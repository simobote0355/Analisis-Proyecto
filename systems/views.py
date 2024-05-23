from django.shortcuts import render
import random
from . import metodos

# Create your views here.
def jacobi_view(request):
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        matriz = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
        b = [random.randint(1, 100) for _ in range(n)]
        return render(request, 'systems/jacobi.html', {'matriz': matriz, 'b': b})
    else:
        return render(request, 'systems/jacobi.html')

def gauss_seidel_view(request):
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        matriz = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
        b = [random.randint(1, 100) for _ in range(n)]
        return render(request, 'systems/gauss_seidel.html', {'matriz': matriz, 'b': b})
    else:
        return render(request, 'systems/gauss_seidel.html')

def sor_view(request):
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        matriz = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
        b = [random.randint(1, 100) for _ in range(n)]
        return render(request, 'systems/sor.html', {'matriz': matriz, 'b': b})
    else:
        return render(request, 'systems/sor.html')
    