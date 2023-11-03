class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.cursos_lecionados = []

    def designar_curso(self, curso):
        self.cursos_lecionados.append(curso)
        curso.professor = self

    def listar_cursos_lecionados(self):
        for curso in self.cursos_lecionados:
            print(f"{self.nome} leciona o curso de {curso.nome}")

class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.professor = None

# Exemplo de uso:
professor1 = Professor("Prof. A")
professor2 = Professor("Prof. B")

curso1 = Curso("Matemática")
curso2 = Curso("História")
curso3 = Curso("Física")

professor1.designar_curso(curso1)
professor1.designar_curso(curso2)
professor2.designar_curso(curso3)

professor1.listar_cursos_lecionados()
professor2.listar_cursos_lecionados()
