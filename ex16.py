horasTrabalhadas: int = 0
valorHora: float = 0.0
percentualDesconto: float = 0.0
numDependentes: int = 0
salarioBruto: float = 0.0
salarioLiquido: float = 0.0
salarioReceber: float = 0.0

horasTrabalhadas = float(input("Digite as horas trabalhadas:"))
valorHora = float(input("Digite o valor por hora:"))
percentualDesconto = float(input("DIgite o percentual de desconto:"))
numDependentes = int(input("Digite o número de dependentes:"))

salarioBruto = valorHora * horasTrabalhadas
salarioLiquido = salarioBruto - (salarioBruto * percentualDesconto/100)
salarioReceber = salarioLiquido + numDependentes * 100

print("Salário a receber: R$", salarioReceber)