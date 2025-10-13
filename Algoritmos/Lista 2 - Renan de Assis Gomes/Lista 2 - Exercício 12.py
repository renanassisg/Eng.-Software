tempo = float(input("INFORME O TEMPO (EM ANOS) QUE FOI MANTIDO O DEPÓSITO: "))
if tempo < 1:
    print ("TAXA DE JUROS IGUAL A 0,55")
else:
    if tempo >= 1 and tempo <2:
        print ("TAXA DE JUROS IGUAL A 0,65")
    else:
        if tempo >= 2 and tempo <3:
            print ("TAXA DE JUROS IGUAL A 0,75")
        else:
            if tempo >= 3 and tempo <4:
                print ("TAXA DE JUROS IGUAL A 0,85")
            else:
                if tempo >= 4 and tempo <5:
                    print ("TAXA DE JUROS IGUAL A 0,90")
                else:
                    if tempo >= 5:
                        print ("TAXA DE JUROS IGUAL A 0,95")