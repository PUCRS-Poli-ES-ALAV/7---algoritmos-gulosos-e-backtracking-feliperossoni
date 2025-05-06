def escalonamento_intervalos(s, f):
    n = len(s)
    
    intervalos = sorted([(s[i], f[i], i) for i in range(n)], key=lambda x: x[1])  # ordena por f
    
    resultado = []
    iteracoes = 0
    fim_ultimo = float('-inf')

    for intervalo in intervalos:
        iteracoes += 1
        inicio, fim, indice_original = intervalo
        if inicio > fim_ultimo:
            resultado.append(indice_original)
            fim_ultimo = fim

    print(f"Número de iterações: {iteracoes}")
    return sorted(resultado) 

s = [4, 6, 13, 4, 2, 6, 7, 9, 1, 3, 9]
f = [8, 7, 14, 5, 4, 9, 10, 11, 6, 13, 12]

indices_sdm = escalonamento_intervalos(s, f)
print("Índices dos intervalos da SDM:", indices_sdm)
