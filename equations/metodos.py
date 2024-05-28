import sympy as sp
import pandas as pd

def biseccion(f, a, b, tol, max_iter):
    # Define symbol
    x = sp.symbols('x')

    # Convert the function string to a Sympy expression
    f_expr = sp.sympify(f)

    # Initialize lists to store function values and errors
    fm = []
    E = []
    Xn_values = []
    iterations = []

    # Evaluate the function at the endpoints
    fi = f_expr.subs(x, a)
    fs = f_expr.subs(x, b)

    # Check if either endpoint is a root
    if fi == 0:
        s = a
        mensaje = f"{a} es raiz de f(x)"
    elif fs == 0:
        s = b
        mensaje = f"{b} es raiz de f(x)"
    elif fs * fi < 0:
        c = 0
        Xm = (a + b) / 2
        fe = f_expr.subs(x, Xm)
        fm.append(fe)
        Xn_values.append(Xm)
        E.append(100)
        iterations.append(c)
        while E[c] > tol and fe != 0 and c < max_iter:
            if fi * fe < 0:
                b = Xm
                fs = f_expr.subs(x, b)
            else:
                a = Xm
                fi = f_expr.subs(x, a)
            Xa = Xm
            Xm = (a + b) / 2
            fe = f_expr.subs(x, Xm)
            fm.append(fe)
            Xn_values.append(Xm)
            Error = abs(Xm - Xa)
            E.append(Error)
            c += 1
            iterations.append(c)
        if fe == 0:
            s = Xm
            mensaje = f"{s} es raiz de f(x)"
        elif Error < tol:
            s = Xm
            mensaje = f"{s} es una aproximacion de un raiz de f(x) con una tolerancia {tol} en {c} iteraciones"
        else:
            s = Xm
            mensaje = f"Fracaso en {max_iter} iteraciones"
    else:
        mensaje = "El intervalo es inadecuado"

    # Create a DataFrame to store the tabla
    tabla = pd.DataFrame({
        'n': iterations,
        'xn': Xn_values,
        'f(xn)': fm,
        'e': E
    })

    return tabla, mensaje


def regla_falsa(f, a, b, tol, iter):
    # Initialize lists to store function values and errors
    fn = []
    xn = []
    E = []
    N = []

    # Define the symbol and the function
    x = sp.symbols('x')
    f_expr = sp.sympify(f)
    f = sp.lambdify(x, f_expr)

    # Initial values
    fa = f(a)
    fb = f(b)
    c = 0
    Error = tol + 1
    
    xn.append(a)
    xn.append(b)
    fn.append(fa)
    fn.append(fb)
    E.append(None)  # No error for the first point
    E.append(None)  # No error for the second point
    N.append(c)
    N.append(c + 1)

    while Error > tol and c < iter:
        c += 1
        x_value = b - (fb * (b - a)) / (fb - fa)
        f_value = f(x_value)
        fn.append(f_value)
        xn.append(x_value)
        
        Error = abs(x_value - xn[-2])
        E.append(Error)
        N.append(c + 1)

        if f_value == 0:
            mensaje = f'{x_value} es raíz de f(x) en {c} iteraciones'
            break
        elif Error < tol:
            mensaje = f"{x_value} es una aproximación de una raíz de f(x) con una tolerancia {tol} en {c+1} iteraciones"
            break
        else:
            if fa * f_value < 0:
                b = x_value
                fb = f_value
            else:
                a = x_value
                fa = f_value

    if Error > tol:
        mensaje = f'Fracaso en {iter} iteraciones'

    # Create a DataFrame to store the table
    tabla = pd.DataFrame({
        'n': N,
        'xn': xn,
        'f(xn)': fn,
        'e': E
    })

    return tabla, mensaje


def punto_fijo(f, g, x0, tol, iter):
    # Initialize lists to store function values and errors
    fn = []
    xn = []
    E = []
    N = []

    # Define symbols
    x = sp.symbols('x')

    # Define functions
    Fun_expr = sp.sympify(f)
    g_expr = sp.sympify(g)

    # Initial values
    x_value = x0
    f_value = Fun_expr.subs(x, x_value)
    c = 0
    Error = 100
    fn.append(f_value)
    xn.append(x_value)
    E.append(None)
    N.append(c)

    # Fixed-point iteration loop
    while Error > tol and f_value != 0 and c < iter:
        x_value = g_expr.subs(x, x_value)
        f_value = Fun_expr.subs(x, x_value)
        fn.append(f_value)
        xn.append(x_value)
        c += 1
        Error = abs(xn[c] - xn[c - 1])
        N.append(c)
        E.append(Error)

        if f_value==0:
            s=x_value
            mensaje=f'{s} es raiz de f(x) en {c} iteraciones'
        elif Error<tol:
            s=x_value
            mensaje=f"{s} es una aproximacion de un raiz de f(x) con una tolerancia {tol} en {c} iteraciones"
        else:
            mensaje=f'Fracaso en {iter} iteraciones'

    # Create a DataFrame to store the tabla
    tabla = pd.DataFrame({
        'n': N,
        'xn': xn,
        'f(xn)': fn,
        'e': E
    })

    return tabla, mensaje

def newton(f, x0, tol, iter):
    # Initialize lists to store function values and errors
    fn = []
    xn = []
    E = []
    N = []

    # Define the symbol and the function
    x = sp.symbols('x')
    f_expr = sp.sympify(f)
    f = sp.lambdify(x, f_expr)

    # Calculate the derivative symbolically
    df_expr = sp.diff(f_expr, x)
    df = sp.lambdify(x, df_expr)

    # Initial values
    x_value = x0
    f_value = f(x_value)
    derivada = df(x_value)
    c = 0
    Error = 100
    fn.append(f_value)
    xn.append(x_value)
    E.append(None)
    N.append(c)

    while Error > tol and f_value != 0 and derivada != 0 and c < iter:
        x_value = x_value - f_value / derivada
        f_value = f(x_value)
        derivada = df(x_value)
        fn.append(f_value)
        xn.append(x_value)
        c += 1
        Error = abs(xn[c] - xn[c - 1])
        N.append(c)
        E.append(Error)

        if f_value==0:
            s=x_value
            mensaje=f'{s} es raiz de f(x) en {c} iteraciones'
        elif Error<tol:
            s=x_value
            mensaje=f"{s} es una aproximacion de un raiz de f(x) con una tolerancia {tol} en {c} iteraciones"
        else:
            mensaje=f'Fracaso en {iter} iteraciones'

    # Create a DataFrame to store the tabla
    tabla = pd.DataFrame({
        'n': N,
        'xn': xn,
        'f(xn)': fn,
        'e': E
    })
    
    return tabla, mensaje

def secante(f, x0, x1, tol, max_iter):
    # Initialize lists to store function values and errors
    fn = []
    xn = []
    E = []
    N = []

    # Define the symbol and the function
    x = sp.symbols('x')
    f_expr = sp.sympify(f)
    f = sp.lambdify(x, f_expr)

    # Initial values
    xn.append(x0)
    xn.append(x1)
    N.append(0)
    N.append(1)
    E.append(None)
    E.append(None)
    f_value0 = f(x0)
    f_value1 = f(x1)
    c = 1
    Error = 100
    fn.append(f_value0)
    fn.append(f_value1)

    while Error > tol and c < max_iter:
        x_next = xn[c] - f_value1 * (xn[c] - xn[c - 1]) / (f_value1 - f_value0)
        f_next = f(x_next)
        xn.append(x_next)
        fn.append(f_next)
        c += 1
        Error = abs(xn[c] - xn[c - 1])
        E.append(Error)
        N.append(c)

        f_value0 = f_value1
        f_value1 = f_next

        if f_next == 0:
            mensaje = f'{x_next} es raiz de f(x) en {c} iteraciones'
        elif Error < tol:
            mensaje = f"{x_next} es una aproximacion de una raiz de f(x) con una tolerancia {tol} en {c} iteraciones"
        else:
            mensaje = f'Fracaso en {max_iter} iteraciones'

    # Create a DataFrame to store the tabla
    tabla = pd.DataFrame({
        'n': N,
        'xn': xn,
        'f(xn)': fn,
        'e': E
    })

    return tabla, mensaje


def raices_multiples(fx, x0, tol, niter):
    # Initialize lists to store function values, derivatives, and errors
    fn = []
    xn = []
    E = []
    N = []

    # Define the symbol and the function
    x = sp.symbols('x')
    f_expr = sp.sympify(fx)
    f = sp.lambdify(x, f_expr, 'numpy')

    # Calculate the derivatives symbolically
    df_expr = sp.diff(f_expr, x)
    d2f_expr = sp.diff(df_expr, x)
    df = sp.lambdify(x, df_expr, 'numpy')
    d2f = sp.lambdify(x, d2f_expr, 'numpy')

    # Initial values
    x_value = x0
    f_value = f(x_value)
    df_value = df(x_value)
    d2f_value = d2f(x_value)
    c = 0
    Error = 100  # Start with a large error to enter the loop

    fn.append(f_value)
    xn.append(x_value)
    E.append(None)
    N.append(c)

    while Error > tol and f_value != 0 and df_value != 0 and c < niter:
        # Update the current value using the modified Newton-Raphson formula
        try:
            x_new = x_value - (f_value * df_value) / (df_value ** 2 - f_value * d2f_value)
        except ZeroDivisionError:
            mensaje = 'División por cero detectada durante la iteración'
            break

        f_value = f(x_new)
        df_value = df(x_new)
        d2f_value = d2f(x_new)

        fn.append(f_value)
        xn.append(x_new)
        c += 1
        Error = abs(x_new - x_value)
        N.append(c)
        E.append(Error)

        # Update the current value
        x_value = x_new

    # Check the result and prepare the message
    if f_value == 0:
        mensaje = f'{x_value} es raíz de f(x) en {c} iteraciones'
    elif Error < tol:
        mensaje = f"{x_value} es una aproximación de una raíz de f(x) con una tolerancia {tol} en {c} iteraciones"
    else:
        mensaje = f'Fracaso en {niter} iteraciones'

    # Create a DataFrame to store the table
    tabla = pd.DataFrame({
        'n': N,
        'xn': xn,
        'f(xn)': fn,
        'e': E
    })

    return tabla, mensaje