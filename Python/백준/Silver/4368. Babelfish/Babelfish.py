import sys

input = sys.stdin.read().splitlines()
dictionary = {}
i = 0
while i < len(input) and input[i] != "":
    eng, foreign = input[i].split()
    dictionary[foreign] = eng
    i += 1
        
i += 1

while i < len(input):
    word = input[i]
    print(dictionary.get(word, "eh"))
    i += 1