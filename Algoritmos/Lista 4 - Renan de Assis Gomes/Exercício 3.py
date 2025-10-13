#3.	Implemente uma função que retorne o menor elemento de um vetor de inteiros.

vetor = []
quantidade = int(input("Quantos valores pretende digitar? "))
if quantidade > 0:
    for i in range (quantidade):
        valores = int(input("Digite os valores que deseja: "))
        vetor.append(valores)
    menor = vetor[0]
    for i in range (len(vetor)):
        if vetor[i] < menor:
            menor = vetor[i]
    print (f"Menor elemento do vetor: {menor}")
else:
    print ("Quantidade de valores inválidas para o vetor.")