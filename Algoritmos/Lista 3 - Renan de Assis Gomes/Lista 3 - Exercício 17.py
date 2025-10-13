#17.	Escrever um algoritmo que lê 10 valores, um de cada vez, e conte quantos deles estão
# no intervalo [10,20] e quantos deles estão fora do intervalo, escrevendo estas informações


dentro = 0
fora = 0
for i in range (10):
    valor = int(input(f"Digite o {i+1}° valor: "))
    if valor >= 10 and valor <= 20:
        dentro = dentro + 1
    else:
        fora = fora + 1
    print(f"Valores dentro do intervalo {10, 20}: {dentro}")
    print(f"Valores fora do intervalo {10, 20}: {fora}")


# Professor eu interpretei "...lê 10 valores, um de cada vez...e quantos deles estão fora do intervalo,
# escrevendo estas informações..." como sendo para colocar o resultado da quantidade de valores dentro e fora
# do intervalo a cada input realizado.