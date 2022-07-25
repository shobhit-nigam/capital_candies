lista = ["aa", "vv", "gg", "aa", "tt", "vv", "aa", "rr", "ee", "tt"]


start_index = lista.index("gg")
end_index = lista.index("ee")

for x in lista[start_index : end_index+1]:
    print("x =", x)


