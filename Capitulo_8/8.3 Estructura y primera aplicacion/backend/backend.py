import numpy as np

def backendPoderoso(entradaValor):
    a = entradaValor * 2 /8 * 7 
    b = np.sin(a)
    c = np.cos(b)
    return c