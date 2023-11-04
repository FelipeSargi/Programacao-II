import os 

print("Programa lê dois números e aponta qual deles é o maior. ")
os.system('cls')
while True:
    try:
        num1 = int(input("Insira o primeiro valor: "))
        break
    except ValueError:
            os.system('cls')
            print("\n\n\tDeu ruim, repete.")
while True:
    try:
        num2 = int(input("Insira o segundo valor: "))
        break
    except ValueError:
            os.system('cls')
            print("\n\n\tDeu ruim, repete. ")

if num1 > num2:
    print(num1,"é o maior")
elif num1 < num2:
    print(num2,"é o maior.")
else:
    print("ambos os valores são iguais. ")
