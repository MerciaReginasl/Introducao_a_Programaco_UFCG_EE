'''
Calculando as raízes de uma equação do segundo grau! Programando 
em Python
'''

import math

print("\n" * 25) ## \n * 25 informa que o programa deve repitir 25 linhas em branco

print("Cálculo das raízes de uma equação do segundo grau: \n\n")

a = float(input("Informe o coeficiente a da equação: "))
b = float(input("Informe o coeficiente b da equação: "))
c = float(input("Informe o coeficiente c da equação: "))

delta = b ** 2 - 4 * a * c

if delta > 0:
	
	x1 = (-b + math.sqrt(delta)) / (2 * a)
	x2 = (-b - math.sqrt(delta)) / (2 * a)
	
	print(f"x1 = {x1:0.0f} e x2 = {x2:0.0f}") ## O f imprime o texto e as chaves irá converter a configuração que os números devem aparecer na saída 
	
elif delta == 0:
	
	x = -b/(2*a)
	
	print(f"x = {x:0.3f}")
	
else:
	print("Não existem raizes reais para esta equação!")
	
print("Fim do Programa!")
