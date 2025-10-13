#6.	Construir um algoritmo que calcule a média aritmética de vários valores inteiros positivos,
# digitados pelo usuário. O final da leitura acontecerá quando for lido um valor negativo

valor = int(input("Digite um valor inteiro e positivo: "))
soma = 0
quantidade = 00
while valor >= 0:
    soma = soma + valor
    quantidade = quantidade + 1
    valor = int(input("Digite um valor: "))
if quantidade > 0:
    media = soma / quantidade
    print(f"Media = {media:5.2f}")