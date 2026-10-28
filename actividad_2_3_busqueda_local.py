"""
Actividad 2.3 — Búsqueda local
Compara Hill Climbing y Simulated Annealing en una función de ejemplo.
No requiere bibliotecas externas.
"""
import math
import random

def objetivo(x):
    return -(x - 3) ** 2 + 10  # máximo en x=3

def hill_climbing(inicio=0.0, pasos=100, delta=0.1):
    x = inicio
    for _ in range(pasos):
        candidatos = [x - delta, x + delta]
        mejor = max(candidatos, key=objetivo)
        if objetivo(mejor) <= objetivo(x):
            break
        x = mejor
    return x, objetivo(x)

def simulated_annealing(inicio=0.0, iteraciones=500, temperatura=5.0, enfriamiento=0.98):
    x = inicio
    mejor_x = x
    t = temperatura
    for _ in range(iteraciones):
        candidato = x + random.uniform(-1.0, 1.0)
        diferencia = objetivo(candidato) - objetivo(x)
        if diferencia > 0 or random.random() < math.exp(diferencia / max(t, 1e-9)):
            x = candidato
        if objetivo(x) > objetivo(mejor_x):
            mejor_x = x
        t *= enfriamiento
    return mejor_x, objetivo(mejor_x)

if __name__ == "__main__":
    random.seed(7)
    x1, v1 = hill_climbing()
    x2, v2 = simulated_annealing()
    print("Función objetivo: f(x) = -(x - 3)^2 + 10")
    print(f"Hill Climbing: x={x1:.3f}, f(x)={v1:.3f}")
    print(f"Simulated Annealing: x={x2:.3f}, f(x)={v2:.3f}")
