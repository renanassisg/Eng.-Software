salario = float(input("DIGITE O SEU SALÁRIO: "))
tempo = float(input("DIGITE O SEUS ANOS DE EMPRESA: "))
if tempo <= 1:
    print ("SALÁRIO REAJUSTADO PARA: ", salario*1.1)
else:
    print ("SALÁRIO REAJUSTADO PARA: ", salario*1.2)