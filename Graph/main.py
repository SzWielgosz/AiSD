from enum import Enum
from typing import Any, Optional, Dict, List, Callable
from Kolejka import Queue
import matplotlib.pyplot as plt
import networkx as nx



def visit(x):
    print(x)

class EdgeType(Enum):
    directed = 1
    undirected = 2

class Vertex:
    data: Any
    index: int

    def __init__(self, data, index):
        self.data = data
        self.index = index

class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, source, destination, weight: Optional[float]):
        self.source = source
        self.destination = destination
        self.weight = weight

class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self, adjacencies):
        self.adjacencies = adjacencies

    def create_vertex(self, data: Any): #wierzcholek
        self.adjacencies[Vertex(data, len(self.adjacencies))] = []

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None: #krawerdz skierowana
        self.adjacencies[source].append(Edge(source, destination, weight))

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None: #krawedz nieskierowana
        self.adjacencies[source].append(Edge(source, destination, weight))
        self.adjacencies[destination].append(Edge(destination, source, weight))

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if edge.name == "directed":
            self.add_directed_edge(source, destination, weight)
        else:
            self.add_undirected_edge(source, destination, weight)

    def traverse_breadth_first(self, visit: Callable[[Any], None]) -> None:
        klucze = [i for i in self.adjacencies]
        odwiedzone = []
        queue = Queue()
        queue.enqueue(klucze[0])
        while len(queue) != 0:
            x = queue.dequeue()
            visit(x)
            odwiedzone.append(x)
            for neighbour in self.adjacencies[x]:
                if neighbour.destination not in odwiedzone:
                    queue.enqueue(neighbour.destination)

    def traverse_depth_first(self, visit: Callable[[Any], None]):
        klucze = [x for x in self.adjacencies.keys()]
        odwiedzone = []
        self.dfs(klucze[0], odwiedzone, visit)

    def dfs(self, v: Vertex, visited: List[Vertex], visit: Callable[[Any], None]):
        visit(v)
        visited.append(v)
        for neighbour in self.adjacencies[v]:
            if neighbour.destination not in visited:
                self.dfs(neighbour.destination, visited, visit)

    def showUndirected(self) -> None:
        G = nx.Graph()
        klucze = [i for i in self.adjacencies]
        visited = []
        i = 0
        while i != len(klucze):
            if klucze[i] not in visited:
                for j in self.adjacencies[klucze[i]]:
                    G.add_edge(j.source.data, j.destination.data)
            i += 1

        pos = nx.spring_layout(G)
        nx.draw(G, pos, node_color='cyan', with_labels=True)

        plt.show()


class GraphPath:
    visited: List[Vertex]
    path: List[Vertex]

    def __init__(self):
        self.visited = []

    def wszerz(self, graf: Graph, poczatek: Vertex, koniec: Vertex):
        queue = Queue()
        queue.enqueue([poczatek])
        while queue:
            x = queue.dequeue()
            x_vertex = x.value[-1]
            for neighbour in graf.adjacencies[x_vertex]:
                if neighbour.destination not in self.visited:
                    x_new = x.value.copy()
                    x_new.append(neighbour.destination)
                    self.visited.append(neighbour.destination)
                    queue.enqueue(x_new)
                    if neighbour.destination == koniec:
                        self.path = x_new


graf = Graph({})

graf.create_vertex("Korsze")
graf.create_vertex("Ketrzyn")
graf.create_vertex("Bartoszyce")
graf.create_vertex("Lankiejmy")
graf.create_vertex("Olsztyn")
graf.create_vertex("Malenkowo")
graf.create_vertex("Malinkowo")

klucze = [i for i in graf.adjacencies]

graf.add(EdgeType(1), klucze[0], klucze[1])
graf.add(EdgeType(1), klucze[0], klucze[3])
graf.add(EdgeType(1), klucze[1], klucze[2])
graf.add(EdgeType(1), klucze[2], klucze[3])
graf.add(EdgeType(1), klucze[2], klucze[4])
graf.add(EdgeType(1), klucze[4], klucze[5])
graf.add(EdgeType(1), klucze[4], klucze[6])
graf.add(EdgeType(1), klucze[5], klucze[6])


graf.showUndirected()