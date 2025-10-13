#2.	Implemente uma função que retorne o maior elemento de um vetor de inteiros.

vetor = []
quantidade = int(input("Quantos valores pretende digitar? "))
if quantidade > 0:
    for i in range (quantidade):
        valores = int(input("Digite os valores que deseja: "))
        vetor.append(valores)
    maior = vetor[0]
    for i in range (len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]
    print (f"Maior elemento do vetor: {maior}")
else:
    print ("Quantidade de valores inválidas para o vetor.")