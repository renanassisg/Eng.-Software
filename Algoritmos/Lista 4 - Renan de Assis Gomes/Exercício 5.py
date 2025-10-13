#Escrever uma função que recebe por parâmetro um vetor de inteiros e retorna a soma de seus elementos.

vetor = []
quantidade = int(input("Quantos valores pretende digitar? "))
soma = 0
if quantidade > 0:
    for i in range (quantidade):
        valores = int(input("Digite os valores que deseja: "))
        vetor.append(valores)
    for i in range (len(vetor)):
        soma = soma + vetor[i]
    print (vetor)
    print (f"Soma total dos valores do vetor = {soma}")
else:
    print("Valor inválido")