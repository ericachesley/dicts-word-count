# put your code here.
import sys

def count_words(filename):
    active_file = open(filename)
    counter = {}

    for line in active_file:
        words = line.rstrip().split(" ")

        for word in words:
            word = word.lower().strip(",").strip(".").strip("?")
            counter[word] = counter.get(word, 0) + 1

    return counter

for word, quantity in count_words(sys.argv[1]).items():
    print(word, quantity)