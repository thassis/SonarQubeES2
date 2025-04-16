from aluno import Aluno

def saudacao(nome):
    print("Bem-vindo, " + nome + "!")

def saudacao_formal(nome):  # função nunca utilizada
    print("É um prazer tê-lo conosco, " + nome + ".")

aluno1 = Aluno("Ana", 20, [7.5, 8.0, 6.5])
aluno2 = Aluno("João", 22, [5.0, 6.0, 7.0])

aluno1.imprimir_dados()
aluno2.imprimir_dados()

