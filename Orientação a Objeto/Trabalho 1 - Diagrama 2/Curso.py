class Curso:

    def __init__(self):
        self.__id = None
        self.__descricao = None
        self.__professor = []
        self.__disciplina = []

    def __str__(self):
        return self.getDescricao()

    def addDisciplina(self, disciplina):
        self.__disciplina.append(disciplina)

    def removeDisciplina(self, disciplina):
        self.__disciplina.remove(disciplina)

    def getDisciplina(self):
        return self.__disciplina

    def addProfessor(self, professor):
        self.__professor.append(professor)

    def removeProfessor(self, professor):
        self.__professor.remove(professor)

    def getProfessor(self):
        return self.__professor

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
        for professor in self.getProfessor():
            print(f"Professor: {professor}")
        for disciplina in self.getDisciplina():
            print(f"Disciplina: {disciplina}")