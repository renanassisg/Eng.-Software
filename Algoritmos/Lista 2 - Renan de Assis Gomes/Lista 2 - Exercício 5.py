num = int(input("DIGITE UM NÚMERO: "))
resto = num%10
if resto == 0:
    print("NÚMERO É DIVISÍVEL POR 10, PORTANTO METADE É: ",num/2)
else:
    print("O NÚMERO DIGITADO NÃO TERMINA COM 0")