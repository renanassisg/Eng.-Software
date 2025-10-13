#1.	Escrever uma função que receba um vetor com 10 valores e retorne quantos destes valores
# são negativos.
funcao = []
negativos = 0
for i in range (10):
    valores = int (input("Digite um valor: "))
    funcao.append(valores)
for i in range (len(funcao)):
    if funcao[i] < 0:
        negativos = negativos +1
print(f"Total de números negativos = {negativos}")


