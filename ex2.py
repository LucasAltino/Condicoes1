num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

if  num1 < num2:
    print("O menor número é",num1,"e o maior é",  num2)
elif    num1 > num2:
    print("O maior número é", num1, "e o menor é", num2)
else:
    print("Os números são iguais")