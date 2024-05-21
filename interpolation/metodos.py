import sympy as sp
import numpy as np

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