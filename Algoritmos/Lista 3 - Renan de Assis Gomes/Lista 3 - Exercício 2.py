#2.	Escreva um algoritmo que leia 20 valores e encontre o maior e o menor deles.
# Mostre o resultado.

for i in range(20):
    numero = int(input(f"Digite o {i+1}° numero: "))
    if i == 0:
        maior = numero
        menor = numero
    if numero > maior:
        maior = numero
    else:
        if numero < menor:
            menor = numero
print(f"Maior = {maior}")
print(f"Menor = {menor}")