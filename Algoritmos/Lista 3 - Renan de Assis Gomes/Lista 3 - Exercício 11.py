#11.	Escrever um algoritmo que leia um número não determinado de valores e calcule a
# média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores
# negativos e o percentual de valores negativos e positivos. Mostre os resultados.

valor = int(input("DIGITE UM VALOR: "))
if valor == 0:
    print ("Valor inválido para iniciar")
else:
    soma = 0
    positivos = 0
    negativos = 0
    quantidade =0
    while valor != 0:
        quantidade = quantidade + 1
        soma = soma + valor
        if valor > 0:
            positivos = positivos + 1
        else:
            negativos = negativos + 1
        valor = int(input("DIGITE UM VALOR: "))
    media = soma / quantidade
    percnegativos = negativos * 100 / quantidade
    percpositivos = positivos * 100 / quantidade
    print (f"Média = {media:5.2f}")
    print(f"Quantidade de positivos = {positivos}")
    print(f"Quantidade de negativos = {negativos}")
    print(f"Percentual positivos = {percpositivos:5.2f}%")
    print(f"Percentual negativos = {percnegativos:5.2f}%")



