lista = ["aa", "vv", "gg", "aa", "tt", "vv", "aa", "rr", "ee", "tt"]

# list for storing the indices
list_aa = []

for i in range(len(lista)):
    if lista[i] == "aa":
        list_aa.append(i)

    if len(list_aa) == 2:
        break

print(list_aa)

    
    


