'''Calculo do fatorial de um número natural'''

numero = int(input("Informe um número natural: "))
fatorial = 1
for fator in range (1, numero+1, 1):
	fatorial *= fator
print(f"O fatorial de {numero} é {fatorial}")
