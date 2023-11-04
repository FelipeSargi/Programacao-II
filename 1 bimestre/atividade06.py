nome = []
nota = []
soma = 0
relatorio = {
    "Nome": nome,
    "Nota": nota

}

for cont in range(1,4):
    add = input("Digite o nome do aluno: ")
    nome.append(add)
    ad = int(input("Digite a nota do aluno: "))
    nota.append(ad)
    soma = soma + ad
    print(relatorio)

soma = soma/3
print(soma)

