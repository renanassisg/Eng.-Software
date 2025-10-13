num1 = float(input("DIGITE O PRIMEIRO NÚMERO: "))
num2 = float(input("DIGITE O SEGUNDO NÚMERO: "))
num3 = float(input("DIGITE O TERCEIRO NÚMERO: "))
num4 = float(input("DIGITE O QUARTO NÚMERO: "))
if num1 < num2:
    if num1 < num3:
        if num1 < num4:
            print("MENOR NÚMERO É: ",num1)
        else:
            print("MENOR NÚMERO É: ", num4)
    else:
        if num3 < num4:
            print("MENOR NÚMERO É: ", num3)
        else:
            print("MENOR NÚMERO É: ", num4)
else:
    if num2 < num3:
        if num2 < num4:
            print("MENOR NÚMERO É: ", num2)
        else:
            print("MENOR NÚMERO É: ", num4)
    else:
        if num3 < num4:
            print("MENOR NÚMERO É: ", num3)
        else:
            print("MENOR NÚMERO É: ", num4)