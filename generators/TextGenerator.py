__author__ = 'Артём'
import re
from datastructures import Graph


class TextGenerator:
    def __init__(self):
        self.g = Graph()

    def read_file(self, path):
        file = open(path)
        i = 1
        for line in file:
            self.process_line(line)
            print(str(i))
            i += 1

    def process_line(self, line):
        """split by ,:- whitespaces, leave ., ..., !, ?"""
        arr = re.split("[\—\-\,\s\"\:\[\]]+", line)
        for i in range(1,len(arr)):
            if arr[i-1][:-1] != '.' or arr[i-1][:-1] != '!' or arr[i-1][:-1] != '?':
                self.g.add_pair(arr[i-1].lower(), arr[i].lower())

    def make_text(self, words_count):
        last = self.g.random_word()
        buffer = last
        for i in range(0, words_count):
            last = self.g.next_word(last)
            if last is None:
                last = self.g.random_word()
            buffer = buffer + " " + last
        return buffer

