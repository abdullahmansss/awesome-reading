# 5. Ask the user to enter a list of strings. Create a new list that consists of those strings with their
# first characters removed.

L = input('Enter a list of strings: ').split()
L = [x[1:] for x in L]
print(L)
