#7.	Escrever a função que recebe por parâmetro uma string e um caracter. e a função deve retornar
# os primeiros caracteres da string até encontrar o caracter passado por parâmetro.

string = input("Digite a palavra que deseja: ")
caracter = input("Digite o caractetér: ")
i = 0
while string[i] != caracter:
    print (string[i], end="")
    i = i + 1
print(string[i])
