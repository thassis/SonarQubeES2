class Aluno:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas
        temp = 0  # variável não utilizada (code smell)

    def media(self):
        if len(self.notas) > 0:
            return sum(self.notas) / len(self.notas)
        else:
            return 0

    def imprimir_dados(self):
        print("Nome do aluno: " + self.nome)
        print("Idade do aluno: " + str(self.idade))
        print("Notas do aluno: " + str(self.notas))
        print("Média: " + str(self.media()))

