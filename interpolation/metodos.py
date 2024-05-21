import sympy as sp
import numpy as np
from scipy.linalg import solve

def vandermonde(puntos):
    A=np.vander(puntos['x'])
    inversa=np.linalg.inv(A)
    b=np.array(puntos['y']).reshape(-1,1)
    a=inversa@b
    x=sp.Symbol('x')
    n=len(a)
    pol=0
    for i in range(n):
        pol+=a[i][0]*x**(n-i-1)
    
    return pol
    
def newton_inter(puntos):
    x = np.array(puntos['x'])
    y = np.array(puntos['y'])
    n = x.size

    D = np.zeros((n, n + 1))
    D[:, 0] = x 
    D[:, 1] = y.T

    for i in range(1, n):
        aux0 = D[i - 1:n, i]
        aux = np.diff(aux0)
        aux2 = x[i:n] - x[0:n - i]
        D[i:n, i + 1] = aux / aux2.T
        
    return D

def lagrange(puntos):
    x = puntos['x']
    y = puntos['y']
    
    n = len(x)
    Tabla = np.zeros((n, n))
    pol = np.zeros_like(x)

    for i in range(n):
        Li = 1
        den = 1
        for j in range(n):
            if j != i:
                paux = np.poly1d([1, -x[j]])
                Li *= paux
                den *= (x[i] - x[j])
        Tabla[i, :] = y[i] * Li / den
        pol = pol.astype(float) + Tabla[i, :]

    return pol

def spline(puntos, grado):
    x = np.array(puntos['x'])
    y = np.array(puntos['y'])
    n = len(x)
    A = np.zeros(((grado + 1) * (n - 1), (grado + 1) * (n - 1)))
    b = np.zeros((grado + 1) * (n - 1))
    cua = x**2
    cub = x**3
    
    if grado == 1:
        c = 0
        h = 0
        for i in range(n - 1):
            A[h, c] = x[i]
            A[h, c + 1] = 1
            b[h] = y[i]
            c += 2
            h += 1
        
        c = 0
        for i in range(1, n):
            A[h, c] = x[i]
            A[h, c + 1] = 1
            b[h] = y[i]
            c += 2
            h += 1
    
    elif grado == 2:
        c = 0
        h = 0
        for i in range(n - 1):
            A[h, c] = cua[i]
            A[h, c + 1] = x[i]
            A[h, c + 2] = 1
            b[h] = y[i]
            c += 3
            h += 1
        
        c = 0
        for i in range(1, n):
            A[h, c] = cua[i]
            A[h, c + 1] = x[i]
            A[h, c + 2] = 1
            b[h] = y[i]
            c += 3
            h += 1
        
        c = 0
        for i in range(1, n - 1):
            A[h, c] = 2 * x[i]
            A[h, c + 1] = 1
            A[h, c + 3] = -2 * x[i]
            A[h, c + 4] = -1
            b[h] = 0
            c += 3
            h += 1
        
        A[h, 0] = 2
        b[h] = 0
    
    elif grado == 3:
        c = 0
        h = 0
        for i in range(n - 1):
            A[h, c] = cub[i]
            A[h, c + 1] = cua[i]
            A[h, c + 2] = x[i]
            A[h, c + 3] = 1
            b[h] = y[i]
            c += 4
            h += 1
        
        c = 0
        for i in range(1, n):
            A[h, c] = cub[i]
            A[h, c + 1] = cua[i]
            A[h, c + 2] = x[i]
            A[h, c + 3] = 1
            b[h] = y[i]
            c += 4
            h += 1
        
        c = 0
        for i in range(1, n - 1):
            A[h, c] = 3 * cua[i]
            A[h, c + 1] = 2 * x[i]
            A[h, c + 2] = 1
            A[h, c + 4] = -3 * cua[i]
            A[h, c + 5] = -2 * x[i]
            A[h, c + 6] = -1
            b[h] = 0
            c += 4
            h += 1
        
        c = 0
        for i in range(1, n - 1):
            A[h, c] = 6 * x[i]
            A[h, c + 1] = 2
            A[h, c + 4] = -6 * x[i]
            A[h, c + 5] = -2
            b[h] = 0
            c += 4
            h += 1
        
        A[h, 0] = 6 * x[0]
        A[h, 1] = 2
        b[h] = 0
        h += 1
        A[h, c] = 6 * x[-1]
        A[h, c + 1] = 2
        b[h] = 0
    
    val = solve(A, b)
    tabla = val.reshape((n - 1, grado + 1))
    
    return tabla