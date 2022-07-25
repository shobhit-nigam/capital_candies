# list references 
lista = ["ironman", "captain", "Hulk", "THOR", "black widow"]
marvel = ["magneto", "wolverine", lista.copy()]
listb = lista.copy()

print("lista =", lista)
print("listb =", listb)
print("marvel =", marvel)

lista.sort()
lista.insert(2, "hawkeye")
lista.append("wanda")
print("after making the chnages")

print("lista =", lista)
print("listb =", listb)
print("marvel =", marvel)
