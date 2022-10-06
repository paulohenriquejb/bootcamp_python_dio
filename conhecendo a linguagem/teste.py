entrada = input().split(' ')

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])


ICM = distancia/(diametro1+diametro2)

print(round(ICM,2))