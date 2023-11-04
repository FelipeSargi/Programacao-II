class Curso:
    
    def __init__(self, nome, codigo):
        self.nome = nome 
        self.codigo = codigo 
        self.professor = None 

   
    def designar_professor(self, professor):
        self.professor = professor 


class Professor:
    
    def __init__(self, nome, matricula):
        self.nome = nome 
        self.matricula = matricula
        self.cursos = [] 
    
    def lecionar_curso(self, curso):
        self.cursos.append(curso) 

    
    def listar_cursos(self):
        print(f"O professor {self.nome} leciona os seguintes cursos:")
        for curso in self.cursos: 
            print(f"- {curso.nome} ({curso.codigo})")


prof1 = Professor("Zé", "789")
prof2 = Professor("Marcos", "2") 

curso1 = Curso("Filosofia", "F1")
curso2 = Curso("Portugues", "P0")
curso3 = Curso("Matematica", "M4")



curso1.designar_professor(prof1)
curso2.designar_professor(prof2)
curso3.designar_professor(prof1)


prof1.lecionar_curso(curso1)
prof1.lecionar_curso(curso2)
prof2.lecionar_curso(curso3)


prof1.listar_cursos()
prof2.listar_cursos()