class Instituicao:

    def __init__(self):
        self.__id = None
        self.__descricao = None
        self.__turmas = []

    def __str__(self):
        return self.getDescricao()

    def addTurma(self, turma):
        self.__turmas.append(turma)

    def removeTurma(self, turma):
        self.__turmas.remove(turma)

    def getTurma(self):
        return self.__turmas

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getDescricao(self):
        return self.__descricao

    def setDescricao(self, descricao):
        self.__descricao = descricao


    def toPrint(self):
        print(f"ID: {self.getId()}")
        print(f"Descrição: {self.getDescricao()}")
        for turma in self.getTurma():
            print(f"Turmas: {turma}")


