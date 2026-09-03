cat1: int = 0
cat2: int = 0
hip: int = 0

cat1 = float(input("Digite o cateto adjascente:"))
cat2 = float(input("Digite o cateto oposto:"))

hip =( cat1 **2 + cat2 **2)**0.5
print("A hipotenusa é", round(hip))