#add adiciona a uma lista, se for apenas um objeto utilizamos o set
#remove deleta da lista
#set configura uma opção
#get puxa a informação já cadastrada

from Curso import Curso
from Professor import Professor
from Aluno import Aluno
from Turma import Turma
from Situacao import Situacao
from Diario import Diario
from Instituicao import Instituicao
from Disciplina import Disciplina
from Curso import Curso

d = Disciplina()
d.setId("OO")
d.setDescricao("Orientação a objetos")

t = Curso()
t.setId("ENG.SOFT 2025")
t.setDescricao("Engenharia de Software")

d.setCurso(t)

t.addDisciplina(d)

t.toPrint()

d.toPrint()

#ID de cada classe
#Como filtrar as informações da classe
#A forma de deixar a classe abstrata é de queal forma
#__str__ como é

# O professor explico que devemos fazer os for e while para varrer lista, e depois ele utilizou o try, except e finally para tratar erros,
#porém ele utilizou isso no main, porque?
# Também usou dentro do main o open write, mas como banco de dados não deveria utiliza-lo dentro do set.7
