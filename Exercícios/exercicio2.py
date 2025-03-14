# O código abaixo é um contador que deve continuar até que o número inserido seja igual a 10. Há um erro lógico no loop.


num = int(input("Digite um número: "))

while num != 10:
    print("Número diferente de 10. Digite novamente.")
    num = int(input("Digite um número: "))
    
print("Você digitou o número correto!")