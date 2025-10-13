num1 = int(input("DIGITE UM NÚMERO ENTRE 1 E 10: "))
num2 = int(input("DIGITE OUTRO NÚMERO ENTRE 1 E 10: "))
if num1 < 1 or num1 > 10:
    print("VALOR INVÁLIDO")
else:
    if num2 < 1 or num2 > 10:
        print("VALOR INVÁLIDO")
    else:
        if (num1 + num2) < 8:
            print("RESULTADO: ", (num1 + num2) / 2)
        else:
            if (num1 + num2) == 8:
                print("RESULTADO: ", (num1 * num2))
            else:
                if num1 > num2:
                    print("RESULTADO: ", (num1 / num2))
                else:
                    print("RESULTADO: ", (num2 / num1))

