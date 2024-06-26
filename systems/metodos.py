import numpy as np
import pandas as pd

def jacobi(a, b, x0, tol, iter_max, norma):
    diagonal = np.diag(np.diag(a))
    inferior = -np.tril(a, k=-1)
    superior = -np.triu(a, k=1)
    
    inversa = np.linalg.inv(diagonal)
    t = inversa @ (inferior + superior)
    c = inversa @ b
    
    radio=max(abs(np.linalg.eigvals(t)))
    
    i = 0
    errores = []
    soluciones = []
    iter=[]
    iter.append(i)
    while i < iter_max:
        x = t @ x0 + c
    
        error = np.linalg.norm(x - x0, ord=norma)
        errores.append(error)
        soluciones.append(x)
        
        if error < tol:
            mensaje=f"La solución ha convergido {x} con una tolerancia de {tol} después de {i+1} iteraciones."
            break
        
        x0 = x
        i += 1  
        iter.append(i)
    
    else:
        mensaje=f"El método no converge después de {iter_max} iteraciones."

    tabla = pd.DataFrame({'Iteración': [i for i in range(len(soluciones))],
                               'Error': errores,
                               'Solución': soluciones})
    
    return tabla, mensaje, radio, t, c

def gauss_seidel(a, b, x0, tol, iter_max, norma):
    diagonal = np.diag(np.diag(a))
    inferior = -np.tril(a, k=-1)
    superior = -np.triu(a, k=1)
    
    inversa = np.linalg.inv(diagonal-inferior)
    t = inversa @ superior
    c = inversa @ b

    radio=max(abs(np.linalg.eigvals(t)))

    i = 0
    errores = []
    soluciones = []
    iter=[]
    iter.append(i)
    while i < iter_max:
        x = t @ x0 + c
    
        error = np.linalg.norm(x - x0, ord=norma)
        errores.append(error)
        soluciones.append(x)
        
        if error < tol:
            mensaje=f"La solución ha convergido {x} con una tolerancia de {tol} después de {i+1} iteraciones."
            break
        
        x0 = x
        i += 1  
        iter.append(i)
    
    else:
        mensaje=f"El método no converge después de {iter_max} iteraciones."

    tabla = pd.DataFrame({'Iteración': [i for i in range(len(soluciones))],
                               'Error': errores,
                               'Solución': soluciones})
    
    return tabla, mensaje, radio, t, c

def sor(a, b, x0, tol, iter_max, norma, w):
    if w==1:
        print("Gauss-Seidel")
        return gauss_seidel(a, b, x0, tol, iter_max, norma)
    if w>1 and w<2:
        return
    else:
        diagonal = np.diag(np.diag(a))
        inferior = -np.tril(a, k=-1)
        superior = -np.triu(a, k=1)
        
        inversa = np.linalg.inv(diagonal-w*inferior)
        t = inversa @ ((1-w)*diagonal+w*superior)
        c = (w*inversa)@b

        radio=max(abs(np.linalg.eigvals(t)))

        i = 0
        errores = []
        soluciones = []
        iter=[]
        iter.append(i)
        while i < iter_max:
            x = t @ x0 + c
        
            error = np.linalg.norm(x - x0, ord=norma)
            errores.append(error)
            soluciones.append(x)
            
            if error < tol:
                mensaje=f"La solución ha convergido {x} con una tolerancia de {tol} después de {i+1} iteraciones."
                break
            
            x0 = x
            i += 1  
            iter.append(i)
        
        else:
            mensaje=f"El método no converge después de {iter_max} iteraciones."

        tabla = pd.DataFrame({'Iteración': [i for i in range(len(soluciones))],
                                'Error': errores,
                                'Solución': soluciones})
        
        return tabla, mensaje, radio, t,c

