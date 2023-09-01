import os

lista = [ ]

while True:
        try:
           print("--------------------------------------")
           opcao = int(input("Informe a opção\n1 - Listar os dados.\n2 - Inserir dado\n3 - Apagar dado.\n4 - Editar dado\n5 - Sair:\n"))
           print("--------------------------------------")
           match opcao:
                case 1:
                    os.system('cls')
                    print(lista)
                    
                case 2:
                     print("--------------------------------------")
                     adicionar = int(input("Escolha o item: \n 1 - Coca-Cola\n 2 - X-Tudo\n"))
                     print("--------------------------------------")
                     match adicionar:
                        case 1:  
                            os.system('cls')
                            lista.append("Coca")
                            print("uma coca adicionada")
                            
                        case 2: 
                            os.system('cls')
                            lista.append("x-tudo")
                            print("um x-tudo adicionado")
                            
            
                case 3:
                    print(lista)
                    deletar = input("Qual item você deseja apagar?")
                    match deletar:
                        case "Coca":
                            os.system('cls')
                            lista.remove("Coca")
                            print("Coca removida")
                            
                        case "x-tudo":
                            os.system('cls')
                            lista.remove("x-tudo")
                            print("x-tudo removido")
                            
                case 4:
                   print(lista)
                   editar = input("Qual dado deve ser alterado? ")
                   match editar:
                       case "coca":
                           os.system('cls')
                           lista.remove("Coca")
                           editar = int(input("Escolha o novo item: \n 1 - Coca-Cola\n 2 - X-Tudo\n"))
                           match editar:
                            case 1:  
                                os.system('cls')
                                lista.append("Coca")
                                print("--------------------------------------")
                                print("Uma coca adicionada")
                                print("--------------------------------------")
                                
                            case 2: 
                                os.system('cls')
                                lista.append("x-tudo")
                                print("--------------------------------------")
                                print("Um x-tudo adicionado")
                                print("--------------------------------------")
                                
                case 5:
                   print("falo")
                   break

                   
                         

        except ValueError:
            os.system('cls')
            print("digite um valor valido")

