alunos = {}

for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno {}: ".format(nome)))
    alunos[nome] = nota


soma_notas = sum(alunos.values())


media = soma_notas / len(alunos)

print("Dicionário de Alunos:", alunos)
print("Soma das Notas:", soma_notas)
print("Média das Notas:", media)
