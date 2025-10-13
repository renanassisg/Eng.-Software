from Pessoa import Pessoa

class Aluno (Pessoa):

    def __init__(self):
        super().__init__()
        self.__matricula = None
        self.__anoinicio = None
        self.__semestreinicio = None
        self.__situacao = []
        self.__diario = []

    def __str__(self):
        return self.getNome()

    def addDiario(self, diario):
        self.__diario.append(diario)

    def removeDiario(self, diario):
        self.__diario.remove(diario)

    def getDiario(self):
        return self.__diario

    def addSituacao(self, situacao):
        self.__situacao.append(situacao)

    def removeSituacao(self, situacao):
        self.__situacao.remove(situacao)

    def getSituacao(self):
        return self.__situacao

    def getMatricula(self):
        return self.__matricula

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def getAnoinicio(self):
        return self.__anoinicio

    def setAnoinicio(self, anoinicio):
        self.__anoinicio = anoinicio

    def getSemestreinicio(self):
        return self.__semestreinicio

    def setSemestreinicio(self, semestreinicio):
        self.__semestreinicio = semestreinicio

    def listarDoc(self):
        super().toPrint()
        print(f"Matrícula: {self.getMatricula()}")
        print(f"Ano de Inicio: {self.getAnoinicio()}")
        print(f"Semestre de início: {self.getSemestreinicio()}")

    def toPrint(self):
        print(f"Matrícula: {self.getMatricula()}")
        print(f"Ano de Inicio: {self.getAnoinicio()}")
        print(f"Semestre de início: {self.getSemestreinicio()}")
        for situacao in self.getSituacao():
            print (f"Situação do aluno: {situacao}")
        for diario in self.getDiario():
            print(f"Diário: {diario}")
