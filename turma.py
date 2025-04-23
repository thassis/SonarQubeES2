from aluno import Aluno

class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno):
        if isinstance(aluno, Aluno):
            self.alunos.append(aluno)
        else:
            raise ValueError("O objeto deve ser uma instância da classe Aluno.")

    def calcular_media_turma(self):
        if not self.alunos:
            return 0
        total_notas = sum(aluno.media() for aluno in self.alunos)
        return total_notas / len(self.alunos)

    def listar_alunos(self):
        for aluno in self.alunos:
            print(f"Nome: {aluno.nome}, Idade: {aluno.idade}, Média: {aluno.media()}")

# Exemplo de uso
if __name__ == "__main__":
    turma = Turma("Turma A")
    aluno1 = Aluno("Ana", 20, [7.5, 8.0, 6.5])
    aluno2 = Aluno("João", 22, [5.0, 6.0, 7.0])
    turma.adicionar_aluno(aluno1)
    turma.adicionar_aluno(aluno2)
    print(f"Média da turma {turma.nome}: {turma.calcular_media_turma()}")
    turma.listar_alunos()