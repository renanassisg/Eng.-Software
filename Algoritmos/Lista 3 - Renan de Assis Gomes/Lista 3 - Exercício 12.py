#12.	Escrever um algoritmo que leia uma quantidade desconhecida de números e conte
# quantos
# deles estão nos seguintes intervalos: [0,25], [26,50], [51,75] e [76,100]. A entrada de dados
# deve terminar quando for lido um número negativo.

num = int(input("Digite um número: "))
intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0
if num < 0:
    print ("Número inválido para iniciar, deve inciar com valor maior igual a 0.")
else:
    while num >= 0:
        if num < 26:
            intervalo1 = intervalo1 + 1
        else:
            if num < 51:
                intervalo2 = intervalo2 + 1
            else:
                if num < 76:
                    intervalo3 = intervalo3 + 1
                else:
                    if num < 101:
                        intervalo4 = intervalo4 + 1
        num = int(input("Digite um número: "))
    print (f"Quantidade de valores entre {0, 25}: {intervalo1}")
    print (f"Quantidade de valores entre {26, 50}: {intervalo2}")
    print (f"Quantidade de valores entre {51, 75}: {intervalo3}")
    print (f"Quantidade de valores entre {76, 100}: {intervalo4}")

