class Situacao:

    def __init__(self):
        self.__situacao = None
        self.__anosemestre = None
        self.__alunos = []

    def __str__(self):
        return self.getSituacao()

    def addAluno(self, aluno):
        self.__alunos.append(aluno)

    def removeAluno(self, aluno):
        self.__alunos.remove(aluno)

    def getAluno(self):
        return self.__alunos

    def getSituacao(self):
        return self.__situacao

    def setSituacao(self, situacao):
        self.__situacao = situacao

    def getAnosemestre(self):
        return self.__anosemestre

    def setAnosemestre(self, anosemestre):
        self.__anosemestre = anosemestre

    def toPrint(self):
        print(f"Situação: {self.getSituacao()}")
        print(f"Ano/Semestre: {self.getAnosemestre()}")
        for aluno in self.getAluno():
            print(f"Aluno: {aluno}")