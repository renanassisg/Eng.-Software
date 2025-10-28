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


def listarClasses():


    p = Professor()
    p.setNome("Renan")
    p.setCpf("321654")
    p.setDatanascimento("15/10/2003")
    p.setEmail("asdfasd@comasd")
    p.setIdentidade("321564987.45")
    p.setTelefone("99999-9999")
    p.setEndereco("rua asdasddkjvnsdf")
    p.setMatricula("321321321")
    p.setTitulacaomaxima("mestre")

    o = Turma()
    o.setId("54as6d4as4d")
    o.setAno("2002")
    o.setDescricao("Engenharia de Software")
    o.setSemestre("2002/1")
    o.setProfessor(p)

    p.addTurmas(o)

    c = Curso()
    c.setId("ENGSOFT")
    c.setDescricao("Engenharia de Software")
    c.addProfessor(p)

    p.addCursos(c)

    a = Aluno()
    a.setNome("Osvaldo")
    a.setCpf("15646576")
    a.setDatanascimento("15/10/2053")
    a.setEmail("assdadsdasddasd@cobv.masd")
    a.setIdentidade("3357316.45")
    a.setTelefone("99889-9999")
    a.setEndereco("rua asdaasasd dafgasdg sdjvnsdf")
    a.setMatricula("87313835135")
    a.setAnoinicio("2025")
    a.setSemestreinicio("2025/1")

    s = Situacao()
    s.setSituacao("REPROVADO")
    s.setAnosemestre("2025/1")
    s.addAluno(a)

    a.addSituacao(s)

    v = Diario()
    v.setV1("20")
    v.setV2("30")
    v.setVt("55")
    v.setVs("5")
    v.setFaltas("10")
    v.setAluno(a)
    v.setTurma(o)

    a.addDiario(v)

    o.addDiario(v)

    i = Instituicao()
    i.setId("UNI")
    i.setDescricao("Uniacademia")
    i.addTurma(o)

    o.setInstituicao(i)

    d = Disciplina()
    d.setId("OO")
    d.setDescricao("Orientação a objetos")
    d.addTurma(o)

    o.setDisciplina(d)

    t = Curso()
    t.setId("ENG.SOFT 2025")
    t.setDescricao("Engenharia de Software")
    t.addProfessor(p)

    d.setCurso(t)

    t.addDisciplina(d)

    t.toPrint()
    d.toPrint()
    p.toPrint()
    o.toPrint()
    i.toPrint()
    d.toPrint()
    a.toPrint()
    s.toPrint()
    v.toPrint()

    #ID de cada classe
    #Como filtrar as informações da classe
    #A forma de deixar a classe abstrata é de queal forma
    #__str__ como é

    # O professor explico que devemos fazer os for e while para varrer lista, e depois ele utilizou o try, except e finally para tratar erros,
    #porém ele utilizou isso no main, porque?
    # Também usou dentro do main o open write, mas como banco de dados não deveria utiliza-lo dentro do set.7


if __name__ == '__main__':
    listarClasses()