fa = open("books.txt", "r")

# UTF-8

stra = fa.read(5)
print(stra)

strb = fa.read(5)
print(strb)

fa.close()
