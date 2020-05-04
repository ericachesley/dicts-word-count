# put your code here.
def count_words(filename):
    active_file = open(filename)
    counter = {}

    for line in active_file:
        words = line.rstrip().split(" ")

        for word in words:
            counter[word] = counter.get(word, 0) + 1

    return counter

for word, quantity in count_words('test.txt').items():
    print(word, quantity)