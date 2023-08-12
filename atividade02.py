import os

print("\n\n\tPrograma que calcula seu Índice de Massa Corpórea - IMC.\n\n")
os.system('cls')

while True:
    try:
        altura = float(input("Entre com sua altura: "))
        break
    except ValueError:
        os.system('cls')
        print("Valor inválido, tente novamente. ")

while True:
    try:
        peso = float(input("Entre com seu peso: "))
        break
    except ValueError:
        os.system('cls')
        print("Valor inválido, tente novamente. ")

imc = float(peso/(altura*altura))

if imc < 18.5:
    os.system('cls')
    print("Sua classificação é: MAGREZA")
elif imc >= 18.5 and imc <= 24.9:
    os.system('cls')
    print("Sua classificação é: NORMAL")
elif imc >= 25.0 and imc <= 29.9:
    os.system('cls')
    print("Sua classificação é: SOBRE PESO")
elif imc >= 30.0 and imc <= 39.9:
    os.system('cls')
    print("Sua classificação é: OBESIDADE ")
elif imc >= 40.0:
    os.system('cls')
    print("Sua classificação é: OBESIDADE GRAVE ")
