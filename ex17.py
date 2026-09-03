litrosGastos: float = 0.0
tempoPercurso: float = 0.0
velocidadeMedia: float = 0.0

velocidadeMedia = float(input("Digite a velocidade média durante o trajeto:"))
tempoPercurso = float (input("Digite o tempo de percurso:"))

kmPercorrido = velocidadeMedia * tempoPercurso
litrosGastos = kmPercorrido / 12
print(round(litrosGastos),"litros gastos na viagem")