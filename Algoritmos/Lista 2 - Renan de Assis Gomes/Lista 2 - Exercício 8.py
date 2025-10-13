anoatual = int(input("DIGITE O ANO ATUAL: "))
anonasci = int(input("DIGITE O SEU ANO DE NASCIMENTO: "))
idade = anoatual - anonasci
if idade < 0:
    print ("ANO ATUAL E/OU ANO DE NASCIMENTO INCORRETOS")
else:
    if idade >= 0 and idade <4:
        print ("VOCÊ TEM", idade, "ANOS E É CONSIDERADO UM BEBÊ")
    else:
        if idade >= 4 and idade <12:
            print ("VOCÊ TEM", idade, "ANOS E É CONSIDERADO UMA CRIANÇA")
        else:
            if idade >= 12 and idade <18:
                print ("VOCÊ TEM", idade, "ANOS E É CONSIDERADO UM ADOLESCENTE")
            else:
                if idade >= 18 and idade <65:
                    print ("VOCÊ TEM", idade, "ANOS E É CONSIDERADO UM ADULTO")
                else:
                    if idade >= 65:
                        print ("VOCÊ TEM", idade, "ANOS E É CONSIDERADO UM IDOSO")
