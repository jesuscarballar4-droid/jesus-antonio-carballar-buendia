"""
Actividad 2.5 — Búsqueda heurística: A* y Dijkstra
Compara las rutas halladas en una cuadrícula pequeña.
No requiere bibliotecas externas.
"""
import heapq

# Coordenadas permitidas; una celda bloqueada no se puede visitar.
bloqueadas = {(1, 1), (2, 1)}
inicio = (0, 0)
meta = (3, 3)
ancho = alto = 4

def vecinos(p):
    x, y = p
    for q in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
        if 0 <= q[0] < ancho and 0 <= q[1] < alto and q not in bloqueadas:
            yield q

def heuristica(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def buscar(usar_heuristica):
    cola = [(0, inicio)]
    costo = {inicio: 0}
    padres = {inicio: None}
    expandidos = 0
    while cola:
        _, actual = heapq.heappop(cola)
        expandidos += 1
        if actual == meta:
            ruta = []
            while actual is not None:
                ruta.append(actual)
                actual = padres[actual]
            return list(reversed(ruta)), costo[meta], expandidos
        for sig in vecinos(actual):
            nuevo = costo[actual] + 1
            if nuevo < costo.get(sig, float("inf")):
                costo[sig] = nuevo
                padres[sig] = actual
                prioridad = nuevo + (heuristica(sig, meta) if usar_heuristica else 0)
                heapq.heappush(cola, (prioridad, sig))
    return [], float("inf"), expandidos

for nombre, usa_h in (("Dijkstra", False), ("A*", True)):
    ruta, distancia, expandidos = buscar(usa_h)
    print(f"{nombre}:")
    print("  Ruta:", " -> ".join(map(str, ruta)))
    print("  Costo:", distancia)
    print("  Nodos expandidos:", expandidos, "\n")
print("Las dos búsquedas encuentran una ruta de costo mínimo; A* usa una heurística.")
