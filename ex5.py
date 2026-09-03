import math

#Declaração de variáveis
A: float = 0.0
B: float = 0.0
C: float = 0.0
x1: float = 0.0
x2: float = 0.0

#Início
A = float(input("Digite o valor de A:"))
B = float(input("Digite o valor de B:"))
C = float(input("Digite o valor de C:"))

delta = B ** 2 - 4 * A * C
x1 = (-B + math.sqrt(delta)) / (2 * A)
x2 = (-B - math.sqrt(delta)) / (2 * A)
print("resultado X1:", x1)
print ("resultado X2", x2)
#Fim