# Funções devem ser definidas no topo do arquivo
def calcular_media(notas):
    # Soma todas as notas e divide pela quantidade de notas
    return sum(notas) / len(notas)

print("Sistema Escolar")

# Solicita o nome do aluno ao usuário
nome_aluno = input("Digite o nome do aluno: ")

# Cria uma lista vazia para armazenar as notas do aluno (nome alterado para o plural)
notas = []

# Repete o processo 4 vezes para receber as notas
for i in range(1, 5):
    # Alterado para float para aceitar notas com casas decimais (ex: 7.5)
    # Adicionado um f-string para mostrar qual nota está sendo digitada (1 a 4)
    nota_digito = float(input(f'Digite a nota {i} do aluno: '))
    notas.append(nota_digito)

media = calcular_media(notas)

print('\n===== RELATÓRIO =====')
# Uso de f-strings para formatação mais limpa
print(f'Nome do aluno: {nome_aluno}')
print(f'Notas do aluno: {notas}')
print(f'Média do aluno: {media:.2f}') # Limita a média a 2 casas decimais

if media >= 7:
    print('Situação: Aprovado')
else:
    print('Situação: Reprovado')

# https://github.com/Insta092
