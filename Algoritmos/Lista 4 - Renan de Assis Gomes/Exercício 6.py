#6.	Escrever a função que recebe por parâmetro uma string e um número. A função deve retornar os
# primeiros caracteres da string de acordo com o número passado por parâmetro.


string = input("Digite a palavra que deseja: ")
valor = int(input("Digite o valor: "))
if valor > (len(string)):
    valor = (len(string))
for i in range (valor):
    print (string[i], end="")

