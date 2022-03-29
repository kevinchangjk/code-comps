word = input()

alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lex = [alphabet.index(letter) for letter in word]

print(sum(lex))