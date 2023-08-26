import os
# atividade
while True:
    try:
        nome = input("Digite seu nome: ")
        break
    except ValueError:
        print("Errou feio, errou rude. Tenta outra vez. ")

while True:
    try:
        sobrenome = input("Digite seu sobrenome: ")
        break
    except ValueError:
        print("Errou feio, errou rude. Tenta outra vez. ")

while True:
    try:
        idade = int(input("Digite sua idade: "))
        break
    except ValueError:
        print("Errou feio, errou rude. Tenta outra vez. ")

while True:
    try:
        altura = float(input("Digite sua altura: "))
        break
    except ValueError:
        print("Errou feio, errou rude. Tenta outra vez. ")

while True:
    try:
        peso = float(input("Digite seu peso: "))
        break
    except ValueError:
        print("Errou feio, errou rude. Tenta outra vez. ")

midade = idade >= 18

os.system('cls')

print(nome, sobrenome,"\n\n", idade, "y\n\n", peso,"Kg\n\n", altura,"m\n\n", "maior de idade?", midade)

if idade >= 18:
    print("\n\n\tÉ realmente ",midade,"o papo sobre você ser maior de idade, hein.\n\n")
else:
    print("\n\n\tSempre soube que esse papo de maior de idade era ", midade,"\n\n")