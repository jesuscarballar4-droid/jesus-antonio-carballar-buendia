"""
Actividad 2.6 — Algoritmo genético para TSP (viajante)
Ejemplo educativo pequeño de optimización de una ruta entre ciudades.
"""
import random

random.seed(10)
ciudades = {
    "A": (0, 0),
    "B": (2, 1),
    "C": (5, 2),
    "D": (6, 5),
    "E": (3, 6),
    "F": (1, 4),
}

def distancia(a, b):
    xa, ya = ciudades[a]
    xb, yb = ciudades[b]
    return ((xa-xb)**2 + (ya-yb)**2) ** 0.5

def costo(ruta):
    return sum(distancia(ruta[i], ruta[(i+1) % len(ruta)]) for i in range(len(ruta)))

def crear_individuo():
    ruta = list(ciudades)
    random.shuffle(ruta)
    return ruta

def cruzar(p1, p2):
    n = len(p1)
    i, j = sorted(random.sample(range(n), 2))
    segmento = p1[i:j]
    resto = [c for c in p2 if c not in segmento]
    return resto[:i] + segmento + resto[i:]

def mutar(ruta, prob=0.2):
    ruta = ruta[:]
    if random.random() < prob:
        i, j = random.sample(range(len(ruta)), 2)
        ruta[i], ruta[j] = ruta[j], ruta[i]
    return ruta

poblacion = [crear_individuo() for _ in range(40)]
for generacion in range(100):
    poblacion.sort(key=costo)
    elite = poblacion[:8]
    nueva = elite[:]
    while len(nueva) < 40:
        p1, p2 = random.sample(elite, 2)
        nueva.append(mutar(cruzar(p1, p2)))
    poblacion = nueva

mejor = min(poblacion, key=costo)
print("Mejor ruta encontrada:", " -> ".join(mejor + [mejor[0]]))
print(f"Distancia total aproximada: {costo(mejor):.2f}")
print("Nota: por ser un algoritmo genético, el resultado puede variar al cambiar parámetros.")
