class Empresa:

    def __init__(self):
        self.__id = None
        self.__codigo = None
        self.__razaosocial = None
        self.__endereco = None
        self.__cnpj = None

    def setCnpj(self, cnpj):
        self.__cnpj = cnpj

    def getCnpj(self):
        return self.__cnpj

    def setEndereco(self, endereco):
        self.__endereco = endereco

    def getEndereco(self):
        return self.__endereco

    def setRazaosocial(self, razaosocial):
        self.__razaosocial = razaosocial

    def getRazasocial(self):
        return self.__razaosocial

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def getCodigo(self):
        return self.__codigo

    def toPrint(selfself):
        print(f"")

