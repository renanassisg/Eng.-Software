#4.	Implemente uma função que ordene um vetor de inteiros de tamanho 10.

vetor = []
for i in range (10):
    valores = int (input("Digite um valor: "))
    vetor.append(valores)
for i in range (len(vetor)):
    for j in range (i, len(vetor)):
        if vetor[j] < vetor[i]:
            salvar = vetor[i]
            vetor[i] = vetor[j]
            vetor[j] = salvar
print(vetor)