print("Sistema Escolar")

# Solicita o nome do aluno ao usuário
nome_aluno = input("Digite o nome do aluno: ")

# Cria uma lista vazia para armazenar as notas do aluno
nota = []

# Repete o processo 4 vezes para receber as notas
for i in range(4):

    # Solicita uma nota e converte o valor digitado para número inteiro
    nota_digito = int(input('Digite a nota do aluno: '))

    # Adiciona a nota digitada à lista de notas
    nota.append(nota_digito)


# Função responsável por calcular a média das notas
def calcular_media(nota):

    # Soma todas as notas e divide pela quantidade de notas
    return sum(nota) / len(nota)


media = calcular_media(nota)
print(media)
print('===== RELATÓRIO =====')
print('Nome do aluno:', nome_aluno)
print('Notas do aluno:', nota)
print('Média do aluno:', media)
if media >= 7:
    print('Situacao: Aprovado')
else:
    print('Situacao: Reprovado')
# https://github.com/Insta092