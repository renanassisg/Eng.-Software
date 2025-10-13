class Turma:

    def __init__(self):
        self.__id = None
        self.__descricao = None
        self.__ano = None
        self.__semestre = None
        self.__professor = None
        self.__diarios = []
        self.__instituicao = None
        self.__disciplina = None

    def __str__(self):
        return self.getDescricao()

    def setDisciplina(self, disciplina):
        self.__disciplina = disciplina

    def getDisciplina(self):
        return self.__disciplina

    def setInstituicao(self, instituicao):
        self.__instituicao = instituicao

    def getInstituicao(self):
        return self.__instituicao

    def addDiario (self, diario):
        self.__diarios.append(diario)

    def removeDiario (self, diario):
        self.__diarios.remove(diario)

    def getDiario (self):
        return self.__diarios

    def setProfessor(self, professor):
        self.__professor = professor

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

    def getAno(self):
        return self.__ano

    def setAno(self, ano):
        self.__ano = ano

    def getSemestre(self):
        return self.__semestre

    def setSemestre(self, semestre):
        self.__semestre = semestre


    def toPrint(self):
        print(f"ID: {self.getId()}")
        print(f"Descrição: {self.getDescricao()}")
        print(f"Ano: {self.getAno()}")
        print(f"Semestre: {self.getSemestre()}")
        print(f"Professor: {self.getProfessor()}")
        for diario in self.__diarios:
            print(f"VT: {diario}")
        print(f"Instituição: {self.getInstituicao()}")
        print(f"Disciplina: {self.getDisciplina()}")