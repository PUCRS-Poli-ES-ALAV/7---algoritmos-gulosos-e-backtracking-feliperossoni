def troco(valor, moedas):
    moedas_usadas = []
    count = 0
    
    moedas.sort(reverse=True)  # Ordena as moedas em ordem decrescente

    for i in range(len(moedas)):
        while valor >= moedas[i]:
            valor -= moedas[i]
            count += 1
            moedas_usadas.append(moedas[i])
    print("Numero iterações:", count)
    return moedas_usadas

moedas = [1, 5, 10, 25, 100]
n= 230
n2= 234
moedas2 = [1, 10, 25, 50, 100]

print("Troco para 230 com moedas", moedas)
print("Moedas usadas:", troco(n, moedas.copy()))

print("\nTroco para 234 com moedas", moedas2)
print("Moedas usadas:", troco(n2, moedas2.copy()))