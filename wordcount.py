# put your code here.
import sys
import string

def count_words(filename):
    
    active_file = open(filename)
    counter = {}

    for line in active_file:
        words = line.rstrip().split(" ")

        for word in words:
            word = word.lower().strip(string.punctuation)
            counter[word] = counter.get(word, 0) + 1

    return counter

def reverse_dictionary(dictionary):
    
    reverse = {}

    for key, value in dictionary.items():
        new_values = reverse.get(value, [])
        new_values.append(key)
        reverse[value] = new_values

    return reverse


counted = count_words(sys.argv[1])
if '' in counted:
    del (counted[""])

reverse_counted = reverse_dictionary(counted)
sorted_quantities = sorted(reverse_counted)[::-1]

for quantity in sorted_quantities:
    for word in sorted(reverse_counted[quantity]):
        print(word, quantity)


"""
for word, quantity in counted.items():
    print(word, quantity)
"""


