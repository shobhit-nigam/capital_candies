fa = open("data.txt", "r+")

fa.read(4)
fa.read(5)
print(fa.tell())
fa.close()


