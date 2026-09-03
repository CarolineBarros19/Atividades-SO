#Declaração de variáveis
base: float = 0.0
altura: float = 0.0
area: float = 0.0

#Início
base = float(input("base do triângulo:"))
altura = float(input("altura do triângulo:"))
area = base * altura / 2
print("Área do triângulo:", area)
#Fim