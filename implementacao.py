import heapq

class No:
    def __init__(self, valor):
        self.valor = valor
        self.distancia = float('infinity')
        self.vizinhos = []

    def adiciona_vizinho(self, vizinho, peso):
        self.vizinhos.append((vizinho, peso))

def dijkstra(inicio):
    fila = [(0, inicio)]
    inicio.distancia = 0

    while fila:
        distancia_atual, no_atual = heapq.heappop(fila)

        if distancia_atual > no_atual.distancia:
            continue

        for vizinho, peso in no_atual.vizinhos:
            distancia = distancia_atual + peso

            if distancia < vizinho.distancia:
                vizinho.distancia = distancia
                heapq.heappush(fila, (distancia, vizinho))
 
        print("Distâncias atuais:")
        print(f"No {inicio.valor}: {inicio.distancia}")
        for vizinho, _ in inicio.vizinhos:
            print(f"No {vizinho.valor}: {vizinho.distancia}")

no1 = No(1)
no2 = No(2)
no3 = No(3)
no4 = No(4)

no1.adiciona_vizinho(no2, 1)
no2.adiciona_vizinho(no3, 2)
no3.adiciona_vizinho(no4, 3)
no4.adiciona_vizinho(no1, 4)

dijkstra(no1)