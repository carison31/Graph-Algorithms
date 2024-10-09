from collections import deque

class Graph:
    class Node:
        def __init__(self, value):
            self.value = value  # значение в вершине
            self.neighbors = []  # список соседей (связанные вершины)

        def add_neighbor(self, neighbor):
            """Добавление смежной вершины"""
            self.neighbors.append(neighbor)

    def __init__(self):
        self.nodes = []  # список всех вершин в графе

    def add_node(self, value):
        """Создание и добавление новой вершины (узла) в граф"""
        new_node = self.Node(value)  # Создаем узел через внутренний класс Node
        self.nodes.append(new_node)
        return new_node  # Возвращаем узел 

    def add_edge(self, node1, node2):
        """Создание ребра между двумя узлами графа"""
        node1.add_neighbor(node2)
        node2.add_neighbor(node1)  # Для неориентированного графа добавляем связь в обе стороны

    def bfs(self, start_node):
        """Обход графа в ширину (BFS), начиная с заданного узла"""
        visited = []
        queue = deque([start_node])
        visited.append(start_node)

        while queue:
            node = queue.popleft()

            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)

        return visited
    
    @staticmethod
    def link_to_values(link_list):
        """Из списка ссылок сделать список значений"""
        return list(map(lambda node: node.value, link_list))
    
    def connected_comps(self):
        """Обход всех компонент связности графа"""
        visited = set()  # множество для отслеживания посещённых узлов
        components = []  # список для хранения всех компонент связности

        # Проходим по всем узлам графа
        for node in self.nodes:
            if node not in visited:
                # Если узел не был посещён, запускаем BFS и собираем компоненту связности
                component = self.bfs(node)
                components.append(self.link_to_values(component))  # сохраняем значения узлов компоненты
                visited.update(component)  # добавляем все узлы компоненты в visited

        return components


def main():
    
    # Создаем граф
    graph = Graph()

    # Добавляем узлы
    nodeA = graph.add_node('A')
    nodeB = graph.add_node('B')
    nodeC = graph.add_node('C')
    nodeD = graph.add_node('D')
    nodeE = graph.add_node('E')
    nodeF = graph.add_node('F')  # Узел в другой компоненте
    nodeG = graph.add_node('G')  # Узел в другой компоненте

    # Добавляем ребра (связи между узлами)
    graph.add_edge(nodeA, nodeB)
    graph.add_edge(nodeA, nodeC)
    graph.add_edge(nodeB, nodeD) 
    graph.add_edge(nodeB, nodeC)
    graph.add_edge(nodeC, nodeE)
    graph.add_edge(nodeE, nodeD)
    graph.add_edge(nodeF, nodeG)

    # Выполняем поиск компонент связности
    connected_components = graph.connected_comps()
    print("Connected Components:", connected_components)


if __name__ == "__main__":
    main()