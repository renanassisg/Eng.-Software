#Para transformar esta classe em abstrata é necessário que eu coloque "from abc import ABC, abstractmethod"
# e em seguida "class Pessoa (ABC)", basicamente aqui defini que pessoa é uma classe abstrata (não sofre instancia).

# Lá em baixo vou definir a função que aqui chamei como listarDoc, é o vinculo entre mãe e filha, aqui eu apenas
# escrevo ela, na filha (professor) vou chama-la para apontar o que eu quero daqui.

from abc import ABC, abstractmethod

class Pessoa (ABC):

    def __init__(self):
        self.__nome = None
        self.__cpf = None
        self.__datanascimento = None
        self.__email = None
        self.__endereco = None
        self.__telefone = None
        self.__identidade = None

    def __str__(self):
        return self.getNome

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getCpf(self):
        return self.__cpf

    def setCpf(self, cpf):
        self.__cpf = cpf

    def getDatanascimento(self):
        return self.__datanascimento

    def setDatanascimento(self, datanascimento):
        self.__datanascimento = datanascimento

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getEndereco(self):
        return self.__endereco

    def setEndereco(self, endereco):
        self.__endereco = endereco

    def getTelefone(self):
        return self.__telefone

    def setTelefone(self, telefone):
        self.__telefone = telefone

    def getIdentidade(self):
        return self.__identidade

    def setIdentidade(self, identidade):
        self.__identidade = identidade

#Definindo o metodo como abstrato, isso aqui é o vinculo entre mãe e filha, aqui eu esboço a função e na filha eu a aplico. Isso é um
# exemplo, não necessáriamente eu preciso aplicar.
    @abstractmethod
    def listarDoc(self):
        pass


    def toPrint(self):
        print(f"Nome: {self.getNome()}")
        print(f"CPF: {self.getCpf()}")
        print(f"Endereço: {self.getEndereco()}")
        print(f"Email: {self.getEmail()}")
        print(f"Telefone: {self.getTelefone()}")
        print(f"Identidade: {self.getIdentidade()}")
        print(f"Data de Nascimento: {self.getDatanascimento()} ")


#DUVIDAS:

# A ID É COLOCADA LÁ EM "MAIN" E SERIA EQUIVALENTE AO p CORRETO?
# O que seria a id da instituição, disciplina, turma e curso? Essa Id sendo o P é o próprio computador que deveria entregar,
# não é algo digitável.