for i in range(38):
    globals()["nom_var_" + str(i)] = i+13

print(globals()["nom_var_" + str(5)])
