codigo = int(input("DIGITE SEU CÓDIGO DO CARGO: "))
if codigo > 106 or codigo < 101:
    print("CÓDIGO INVÁLIDO")
else:
    if codigo == 101:
        print("VENDEDOR")
    else:
        if codigo == 102:
            print("ATENDENTE")
        else:
            if codigo == 103:
                print("AUXILIAR TÉCNICO")
            else:
                if codigo == 104:
                    print("ASSISTENTE")
                else:
                    if codigo == 105:
                        print("COORDENADOR DE GRUPO")
                    else:
                        print("GERENTE")

