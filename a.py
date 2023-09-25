import sympy as sp
from sympy.plotting import plot


# Definición de las variables simbólicas
x = sp.symbols('x')

# Función objetivo
Z = "-2*x + 14"

# Restricciones

f1 = "10-1*x"
f2 = "4+0*x"
f3 = "-1 + x"

# Resuelve las restricciones


# Encuentra el valor óptimo de Z


# Muestra la solución
plot(f1, f2, f3, Z, (x, 0, 10))
