num1 = float(input("DIGITE UM NÚMERO REAL: "))
num2 = float(input("DIGITE OUTRO NÚMERO REAL: "))
codigo = int(input("DIGITE UM CÓDIGO ENTRE 1 E 3: "))
if codigo < 1 or codigo > 3:
    print ("CÓDIGO INVÁLIDO")
else:
    if codigo == 1:
        print("RESULTADO: ", num1+num2)
    else:
        if codigo == 2:
            print("RESULTADO: ", num1*num2)
        else:
            print("RESULTADO: ", num1/num2)


