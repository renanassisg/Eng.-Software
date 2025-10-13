#9.	Escrever o algoritmo que leia os valores n1 e n2 e imprima o intervalo fechado
# (incluindo os limites) entre esses dois valores

valor1 = int(input("DIGITE O 1° VALOR: "))
valor2 = int(input("DIGITE O 2° VALOR: "))
if valor1 < valor2:
    while valor1 <= valor2:
        print (valor1)
        valor1 = valor1 + 1
else:
    while valor2 <= valor1:
        print (valor2)
        valor2 = valor2 + 1