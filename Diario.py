class Diario:

    def __init__(self):
        self.__v1 = None
        self.__v2 = None
        self.__vs = None
        self.__vt = None
        self.__faltas = None
        self.__aluno = None
        self.__turma = None

    def __str__(self):
        return self.getVt()

    def setTurma(self, turma):
        self.__turma = turma

    def getTurma(self):
        return self.__turma

    def setAluno(self, aluno):
        self.__aluno = aluno

    def getAluno(self):
        return self.__aluno

    def getV1(self):
        return self.__v1

    def setV1(self, v1):
        self.__v1 = v1

    def getV2(self):
        return self.__v2

    def setV2(self, v2):
        self.__v2 = v2

    def getVs(self):
        return self.__vs

    def setVs(self, vs):
        self.__vs = vs

    def getVt(self):
        return self.__vt

    def setVt(self, vt):
        self.__vt = vt

    def getFaltas(self):
        return self.__faltas

    def setFaltas(self, faltas):
        self.__faltas = faltas


    def toPrint(self):
        print (f"Avaliação V1: {self.getV1()}")
        print (f"Avaliação V2: {self.getV2()}")
        print (f"Avaliação Vs: {self.getVs()}")
        print (f"Nota Final: {self.getVt()}")
        print (f"Faltas: {self.getFaltas()}")
        print (f"Aluno: {self.getAluno()}")
        print (f"Turma: {self.getTurma()}")
