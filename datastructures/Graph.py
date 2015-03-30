__author__ = 'Артём'
from random import randint
from datastructures.Edge import Edge

class Graph():
    def __init__(self):
        self.edges = []

    def add_pair(self, source, destination):
        node = self.__find(source, destination)
        if node is None:
            self.edges.append(Edge(source, destination))
        else:
            node.Count += 1

    def __find(self, source, destination):
        for pair in self.edges:
            if pair.From == source and pair.To == destination:
                return pair
        return None

    def __find_all(self, source):
        result = []
        for pair in self.edges:
            if pair.From == source:
                result.append(pair)
        return result

    def next_word(self, word):
        nodes = self.__find_all(word)
        total = 0
        for pair in nodes:
            total += pair.Count
        if total == 0:
            return None
        drop = randint(1, total)
        for pair in nodes:
            drop -= pair.Count
            if drop <= 0:
                return pair.To
        return None

    def random_word(self):
        drop = randint(0, len(self.edges))
        return self.edges[drop].From
