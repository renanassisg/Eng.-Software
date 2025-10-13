#1.	Escrever um algoritmo que lê 10 valores e conte quantos destes valores são negativos,
# escrevendo esta informação.

quantidade = 0
for i in range(10):
    valor = int(input(f"Digite o valor {i+1}°: "))
    if valor < 0:
        quantidade = quantidade + 1
print(f"Quantidade de negativos = {quantidade}")