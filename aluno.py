class Aluno:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas
        temp = 0  # variável não utilizada (code smell)

    def media(self):
        # Possível divisão por zero (removida a verificação)
        return sum(self.notas) / len(self.notas)

    def imprimir_dados(self):
        # Uso de concatenação de strings em vez de f-strings
        print("Nome do aluno: " + self.nome)
        print("Idade do aluno: " + str(self.idade))
        print("Notas do aluno: " + str(self.notas))
        print("Média: " + str(self.media()))

    # def metodo_sem_uso(self):
    #     # Método que não é usado em lugar nenhum
    #     print("Este método não é utilizado.")