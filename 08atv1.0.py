import random #biblioteca.
import time #biblioteca.
import os #biblioteca.
def cabecario():
    
    os.system('cls') #comando que limpa o terminal.
    print("     Bem Vindo!      \n Hoje é um ótimo dia para testar a sua sorte...\n Sinto que os espíritos estão com um ótimo humor.\n Talvez pescar fosse uma escolha mais rentável, mas não nos preocuparemos com isso. ")
    time.sleep(5)
def soma(num1,num2):
    print(num1,"+",num2, "=", num1+num2)

def sub(num3,num4):
    return num3 - num4

def sorteia():
    os.system('cls')
    num = random.randint(1,3) #Sorteia um númsero entre 1 e 10.
    for x in range(1,6):
        numero = int(input("\n\nDigite um número: ")) #Recebe um numero qualquer.
        
        if numero == num:
            os.system('cls')
            print("Parabéns!") 
            time.sleep(5) #Congela a tela por 5 segundos.
            print("Você acaba de receber a chance de presenciar algo simplesmente inovador. ")
            time.sleep(3)
            soma(1,1)
            time.sleep(3)
            os.system('cls')
            print("Não satisfeito ainda? Não se preocupe, pois você também saberá que: ")
            time.sleep(3)
            resultado = sub(1,1)
            print(resultado,"é par.")
            exit()
        else:
            os.system('cls')
            print("Errou!\n Pense melhor durante alguns segundos antes de tentar outra vez...   ")
            time.sleep(5) #Congela a tela por 5 segundos.
    print("Acabou, tenta de novo, ainda tem tudo pra da errado ")
    
def concorrer():
    os.system('cls')
    print("Antes de tudo...\n\nTens certeza?.")
    time.sleep(2)
    certez = str(input("Sim ou Não?\n"))
    if certez in ["Sim", "s", "SIM", "sim", "si"]:
        sorteia()
    else:
        exit()


cabecario() #função sendo puxada para execução.
concorrer() #função sendo puxada para execução.










