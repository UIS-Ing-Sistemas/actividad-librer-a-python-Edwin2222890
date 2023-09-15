import numpy as np


votos = np.random.randint(1, 31, size=5000) #5k de votos aleadoreos


candidatos, conteo = np.unique(votos, return_counts=True) #conteo de votos


resultados = list(zip(candidatos, conteo)) #conteo en lista


resultados.sort(key=lambda x: x[1], reverse=True) #ordenar

# Imprimir
print("Listado de candidatos por número de votos:")
for i, (candidato, votos) in enumerate(resultados, start=1):
    print(f"{i}. Candidato {candidato}: {votos} votos")