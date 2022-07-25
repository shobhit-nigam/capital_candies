lista = ["aa", "vv", "gg", "aa", "tt", "vv", "aa", "rr", "ee", "tt"]

dict_occ = {}

for i in range(len(lista)):
    if lista[i] not in dict_occ:
        dict_occ[lista[i]] = 1
    else:
        dict_occ[lista[i]] = dict_occ[lista[i]] + 1
    print(dict_occ)
    


