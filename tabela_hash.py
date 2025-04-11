from aluno import Aluno

class Hash:

    def __init__(self, n):
        """ Inicia as variáveis da tabela hash """

        self.linha = 10
        self.coluna = n // 10
        self.vetor = [[[] for _ in range(self.coluna)] for _ in range(self.linha)]
    
    def hash_code1(self, valor):
        """ Retorna o índice da linha """

        return valor % self.linha

    def hash_code2(self, valor):
        """ Retorna o índice da coluna """

        return (valor // self.linha) % self.coluna

    def insert(self, aluno : Aluno):
        """ Insere um novo aluno na tabela """

        c = Aluno.unicode(aluno.nome) 
        i = self.hash_code1(c)
        j = self.hash_code2(c)

        self.vetor[i][j].append(aluno)

    def busca(self, chave):
        """ Busca um aluno a partir do nome """

        c = Aluno.unicode(chave)
        i = self.hash_code1(c)
        j = self.hash_code2(c)

        for aluno in self.vetor[i][j]:

            if aluno.nome == chave:
                return aluno
        
        return None

    def mostrar(self):
        """ Exibe a tabela hash """

        print("\tTabela hash de alunos")
        for i in range(self.linha):
            for j in range(self.coluna):

                if self.vetor[i][j]:
                    print(f"[{i}][{j}] ->")

                    for aluno in self.vetor[i][j]:
                        print(f"\t{aluno}")
                
                else:
                    print(f"[{i}][{j}] ->")
        
        print()