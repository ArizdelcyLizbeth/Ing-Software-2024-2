import matplotlib.pyplot as plt
import numpy as np

# Definimos la funcion a graficar
def mi_funcion(x):
    return np.sin(x)

# Generamos valores x
x = np.linspace(0, 2*np.pi, 100)

# Generamos valores y aplicando la funcion
y = mi_funcion(x)

# Graficar la funcion
plt.plot(x, y)
plt.title('Gráfica de mi función')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()