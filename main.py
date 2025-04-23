from aluno import Aluno
import os  # Importação não utilizada

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

def imprimir_dados_aluno1():
    print("Nome: Ana")
    print("Idade: 20")
    print("Notas: [7.5, 8.0, 6.5]")

def imprimir_dados_aluno2():
    print("Nome: João")
    print("Idade: 22")
    print("Notas: [5.0, 6.0, 7.0]")

# Dados sensíveis
senha = "123456"  # Dados sensíveis no código (security issue)

# Entrada de usuário sem validação (possível problema de segurança)
nome_usuario = input("Digite seu nome: ")
saudacao(nome_usuario)

try:
    resultado = 10 / 2  # Forçando uma exceção
except Exception:  # Exceção genérica (code smell)
    print("Ocorreu um erro.")

print("Depuração: Iniciando o programa...")  # Uso de print para depuração

aluno1 = Aluno("Ana", 20, [7.5, 8.0, 6.5])
aluno2 = Aluno("João", 22, [5.0, 6.0, 7.0])

aluno1.imprimir_dados()
aluno2.imprimir_dados()