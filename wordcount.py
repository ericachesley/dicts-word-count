# put your code here.
import sys
import string

def count_words(filename):
    active_file = open(filename)
    counter = {}

    for line in active_file:
        words = line.rstrip().split(" ")

        for word in words:
            word = strip_punctuation(word.lower())
            counter[word] = counter.get(word, 0) + 1

    return counter

def strip_punctuation(word):
    #puncts = ['.', ',']
    for punct in string.punctuation:
        word = word.strip(punct)
    return word

for word, quantity in count_words(sys.argv[1]).items():
    print(word, quantity)