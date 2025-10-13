horas = int(input("DIGITE O NÚMERO DE HORAS TRABALHADAS SEMANALMENTE: "))
if horas <= 40:
    print("SALÁRIO A RECEBER: R$",horas*15)
else:
    print("SALÁRIO A RECEBER: R$", (horas-40)*21+600)