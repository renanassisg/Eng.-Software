ano = int(input("DIGITE O ANO DO SEU VEÍCULO: "))
peso = int(input("DIGITE O PESO DO VEÍCULO: "))
if ano <= 1970:
    if peso<1200:
        print("VEÍCULO CLASSE 1, TAXA DE REGISTRO 16,50$")
    else:
        if peso >= 1200 and peso <= 1700:
            print("VEÍCULO CLASSE 2, TAXA DE REGISTRO 25,50$")
        else:
                print("VEÍCULO CLASSE 3, TAXA DE REGISTRO 46,50$")
else:
    if ano >= 1971 and ano <= 1979:
        if peso<1200:
            print("VEÍCULO CLASSE 4, TAXA DE REGISTRO 27,00$")
        else:
            if peso >= 1200 and peso <= 1700:
                print("VEÍCULO CLASSE 5, TAXA DE REGISTRO 30,50$")
            else:
                    print("VEÍCULO CLASSE 6, TAXA DE REGISTRO 52,50$")
    else:
        if peso < 1600:
            print("VEÍCULO CLASSE 7, TAXA DE REGISTRO 19,50$")
        else:
            print("VEÍCULO CLASSE 8, TAXA DE REGISTRO 55,50$")