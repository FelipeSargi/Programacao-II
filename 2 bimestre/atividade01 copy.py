import os 
import time 
class Conta_Bancaria:
    def __init__(self,titular, saldo):
        self.titular = titular
        self.saldo = saldo

nome = input("Digite o nome do titular:\n")
if nome != " ":
    os.system('cls')
    nome = Conta_Bancaria(nome,0)
    print("TITULAR CADASTRADO")
    time.sleep(2)
else:
    print("Nome INVALIDO")
    time.sleep(2)

print("\t\tMENU\t\t")
print("1 - Consultar Saldo")
print("2 - Depositar")
print("3 - Sacar ")
print("4 - Sair")
x = input("Escolha uma opção. ")

match x:
    case 1:
        nome.saldo() 
    case 2:
        print("Deposito")
    case 3:
        print("Sacar")
        
    case 4:
        SystemExit
    

