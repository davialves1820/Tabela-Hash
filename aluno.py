
class Aluno:

    def __init__(self, nome, nota):
        """ Inicia as variáveis de aluno """

        self.nome = nome
        self.nota = nota

    @staticmethod
    def unicode(chave):
        """ Método estático que retorna o código hash """

        v = 1
        i = 0
        for c in reversed(chave):
            i += ord(c) * v
            v *= 18

        return i
    
    def __str__(self):
        """ Retorna na forma de string os dados de aluno, para ficar mais facil a exibição """

        return f"Nome: {self.nome}\t Nota: {self.nota}"

