# Faça um programa que calcule o valor a ser pago por uma dívida em atraso. O usuário deve informar o valor original da dívida (ex. R$ 50,00), a quantidade de dias em atraso (ex. 35 dias) e o valor da multa por dia de atraso (ex. R$ 0,25). 

valor_original = float(input('Insira o valor original da dívida: '))
dias_atraso = int(input('Insira a quantidade de dias em atraso: '))
multa_por_dia = float(input('Insira o valor da multa por dia de atraso: '))

valor_multa = dias_atraso * multa_por_dia
valor_total = valor_original + valor_multa

print('O valor da multa é: R$', valor_multa)
print('O valor total a ser pago é: R$', valor_total)
