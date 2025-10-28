from Pessoa import Pessoa

class Professor(Pessoa):

    def __init__(self):
        super().__init__()
        self.__matricula = None
        self.__titulacaomaxima = None
        self.__cursos = []
        self.__turmas = []


    def __str__(self):
        return self.getNome()

    def addTurmas(self, turma):
        self.__turmas.append(turma)

    def removeTurmas(self, turma):
        self.__turmas.remove(turma)

    def getTurmas(self):
        return self.__turmas

    def addCursos(self, curso):
        self.__cursos.append(curso)

    def removeCursos(self, curso):
        self.__cursos.remove(curso)

    def getCursos(self):
        return self.__cursos

    def getMatricula(self):
        return self.__matricula

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def getTitulacaomaxima(self):
        return self.__titulacaomaxima

    def setTitulacaomaxima(self, titulacaomaxima):
        self.__titulacaomaxima = titulacaomaxima


    def listarDoc(self):
        super().toPrint()
        print(f"Matrícula: {self.getMatricula()}")
        print(f"Titulação Máxima: {self.getTitulacaomaxima()}")

    def toPrint(self):
        print(f"Matrícula: {self.getMatricula()}")
        print(f"Titulação Máxima: {self.getTitulacaomaxima()}")
        for curso in self.getCursos():
            print(f"Curso: {curso}")
        for turma in self.getTurmas():
            print(f"Curso: {turma}")