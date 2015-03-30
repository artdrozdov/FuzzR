__author__ = 'Артём'
from generators import TextGenerator
from generators.WordGenerator import WordGenerator
import sys


def text_generator():
    w = TextGenerator()
    w.read_file(sys.argv[1])
    print(w.make_text(200))


def word_generator():
    w = WordGenerator()
    file = open(sys.argv[1])
    for line in file:
        w.add_word(line)
    print("Enter word's length:")
    n = input()
    b = w.generate(int(n))
    print(b)

word_generator()