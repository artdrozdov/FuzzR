__author__ = 'Артём'
from datastructures import Graph


class WordGenerator:

    def __init__(self):
        self.g = Graph.Graph()

    def add_word(self, word):
        for i in range(1, len(word)):
            self.g.add_pair(word[i-1], word[i])

    def generate(self, n):
        last = self.g.random_word()
        buffer = last
        for i in range(0, n):
            last = self.g.next_word(last)
            if last is None:
                last = self.g.random_word()
            buffer = buffer + last
        return buffer


