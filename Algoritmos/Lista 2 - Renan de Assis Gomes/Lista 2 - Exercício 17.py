codigo = int(input("DIGITE O CÓDIGO DO TIPO DA UNIDADE: "))
if codigo < 1 or codigo > 4:
    print("CÓDIGO INVÁLIDO")
else:
    if codigo == 1:
        print ("UNIDADE: CD_ROM (700MB)")
    else:
        if codigo == 2:
            print("UNIDADE: DVD_ROM (4.7GB)")
        else:
            if codigo == 3:
                print("UNIDADE: DVD-9 (8.54GB)")
            else:
                print("UNIDADE: BLU-RAY (25GB)")
