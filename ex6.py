#Declaração de variáveis
x: float = 0.0
y: float = 0.0
aux: float = 0.0

#Início
x = float(input("Digite o valor de X: "))
y = float(input("Digite o valor de Y: "))

aux = x
x = y
y = aux

print("Valor de X:", x)
print("Valor de Y:", y)
#Fim