import os
saldo = 0
class ContaBancaria:
    def __init__ (self,titular):
        self.titular = titular
       # self.saldo = None
        #saldo = 0

    def deposito(self):
        os.system('cls')
        print("ÁREA DE DEPÓSITO")
        valor = float(input("Digite o valor a ser depósitado:\n "))
        if valor > 0:
            saldo = (saldo + valor)
            print(f"{self.valor} foi adicionado com sucesso ao seu saldo. ")
            return
        else:
            print("Valor Inválido.")
            return
        
    def sacar(self):
        os.system('cls')
        print("ÁREA DE SAQUE")
        quantia = float(input("Digite o valor a ser sacado:\n "))
        if saldo > 0:
            saldo = (saldo - quantia)
            print(f"{self.quantia} foi sacado de seu saldo com sucesso. ")
            return
        elif saldo == 0:
            print("Não existe saldo a ser sacado.")
            return
        else:
            print("Valor inválido")
            return
        
    def ver_saldo(self):
        print(saldo)
        print("Titular da conta: ", donoconta.titular)

nome = str(input("Digite o nome do titular da conta: "))
if nome != "":
    donoconta = ContaBancaria(nome)
    print("Cadastrado Realizado")
else:
    print("Nome invalido") 

print("MENU")
print("1 - Consultar Saldo")
print("2 - Depositar")
print("3 - Sacar ")
print("4 - Sair")
x = input("Escolha uma opção. ")

match x:
    case 1:
        donoconta.ver_saldo()
    case 2:
        donoconta.deposito()   
    case 3:
        donoconta.sacar()           
    case 4:
        print("Adeus")
        SystemExit