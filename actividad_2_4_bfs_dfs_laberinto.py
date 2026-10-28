"""
Actividad 2.4 — Búsqueda ciega: BFS y DFS
Recorre un grafo tipo laberinto y muestra la ruta encontrada por cada algoritmo.
"""
from collections import deque

grafo = {
    "Inicio": ["A", "B"],
    "A": ["Inicio", "C", "D"],
    "B": ["Inicio", "E"],
    "C": ["A", "Meta"],
    "D": ["A", "Meta"],
    "E": ["B", "Meta"],
    "Meta": ["C", "D", "E"],
}

def reconstruir(padres, meta):
    ruta = []
    actual = meta
    while actual is not None:
        ruta.append(actual)
        actual = padres[actual]
    return list(reversed(ruta))

def bfs(inicio, meta):
    cola = deque([inicio])
    padres = {inicio: None}
    while cola:
        nodo = cola.popleft()
        if nodo == meta:
            return reconstruir(padres, meta)
        for vecino in grafo[nodo]:
            if vecino not in padres:
                padres[vecino] = nodo
                cola.append(vecino)
    return []

def dfs(inicio, meta):
    pila = [inicio]
    padres = {inicio: None}
    while pila:
        nodo = pila.pop()
        if nodo == meta:
            return reconstruir(padres, meta)
        for vecino in reversed(grafo[nodo]):
            if vecino not in padres:
                padres[vecino] = nodo
                pila.append(vecino)
    return []

print("BFS (búsqueda en anchura):", " -> ".join(bfs("Inicio", "Meta")))
print("DFS (búsqueda en profundidad):", " -> ".join(dfs("Inicio", "Meta")))
print("BFS explora por niveles; DFS profundiza por una rama antes de retroceder.")
