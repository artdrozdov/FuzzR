__author__ = 'Артём'
from random import randint
import sys
import re

class Edge():
    def __init__(self, source, destination):
        self.From = source
        self.To = destination
        self.Count = 1


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
        drop = randint(1, total)
        for pair in nodes:
            drop -= pair.Count
            if drop <= 0:
                return pair.To
        return None

    def random_word(self):
        drop = randint(0, len(self.edges))
        return self.edges[drop].From

g = Graph()


def read_file(path):
    file = open(path)
    i = 1
    for line in file:
        process_line(line)
        print(str(i))
        i += 1


def process_line(line):
    """split by ,:- whitespaces, leave ., ..., !, ?"""
    arr = re.split("[\—\-\,\s\"\:\[\]]+", line)
    for i in range(1,len(arr)):
        if arr[i-1][:-1] != '.' or arr[i-1][:-1] != '!' or arr[i-1][:-1] != '?':
            g.add_pair(arr[i-1].lower(), arr[i].lower())


def make_text(words_count):
    last = g.random_word()
    buffer = last
    for i in range(0, words_count):
        last = g.next_word(last)
        if last is None:
            last = g.random_word()
        buffer = buffer + " " + last
    return buffer


read_file(sys.argv[1])
print(make_text(200))