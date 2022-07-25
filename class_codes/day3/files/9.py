fa = open("books.txt", "r")
lista = fa.readlines()
fa.close()

fb = open("new_books.txt", "w")

for line in lista:
    if "the" in line.lower():
        fb.write(line)

fb.close()




# if line[:3].lower() == "the"
        

