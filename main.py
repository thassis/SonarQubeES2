from aluno import Aluno
from turma import Turma

# Variável global
contador = 0  # Variável global (code smell)

def saudacao(nome):
    # Uso de concatenação de strings
    print("Bem-vindo, " + nome + "!")

def saudacao_formal(nome):  # Função nunca utilizada
    print("É um prazer tê-lo conosco, " + nome + ".")

def incrementar_contador():
    global contador
    contador += 1

def calcular_soma(numeros):
    soma = 0
    for numero in numeros:  # Loop redundante
        soma += numero
    return soma

def imprimir_dados_aluno(aluno):
    # Uso de concatenação de strings em vez de f-strings
    print("Nome do aluno: " + aluno.nome)
    print("Idade do aluno: " + str(aluno.idade))
    print("Notas do aluno: " + str(aluno.notas))
    print("Média: " + str(aluno.media()))

# Dados sensíveis
senha = "123456"  # Dados sensíveis no código (security issue)

# Entrada de usuário sem validação (possível problema de segurança)
nome_usuario = "Thiago"
saudacao(nome_usuario)

try:
    resultado = 10 / 2  # Forçando uma exceção
except Exception:  # Exceção genérica (code smell)
    print("Ocorreu um erro.")

print("Depuração: Iniciando o programa...")  # Uso de print para depuração

aluno1 = Aluno("Ana", 20, [7.5, 8.0, 6.5])
aluno2 = Aluno("João", 22, [5.0, 6.0, 7.0])

imprimir_dados_aluno(aluno1)
imprimir_dados_aluno(aluno2)

turma = Turma("Turma B")
turma.adicionar_aluno(aluno1)
turma.adicionar_aluno(aluno2)
print(f"Média da turma {turma.nome}: {turma.calcular_media_turma()}")
turma.listar_alunos()