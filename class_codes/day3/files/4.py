fa = open("books.txt", "r")

stra = fa.read()
lista = stra.splitlines()
print(lista)
fa.close()
