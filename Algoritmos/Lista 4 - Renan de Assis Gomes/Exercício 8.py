#8.	Implemente uma função que, dado um valor, retorne se esse valor pertence ou não a um
# vetor de inteiros.

vetor = [1,2,3,4,6,7,8,9]
valor = int(input("Digite o valor que queira verificar: "))
check = False
for i in range (len(vetor)):
    if vetor[i] == valor:
        check = True
if check == True:
    print ("Pertence")
else:
    print ("Não pertence")
