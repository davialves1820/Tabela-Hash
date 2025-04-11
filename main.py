from tabela_hash import Hash
from aluno import Aluno

def main():

    h = Hash(30)
    a1 = Aluno("Davi", 9)
    a2 = Aluno("Daniel", 8)
    a3 = Aluno("Maria", 7)
    h.insert(a1)
    h.insert(a2)
    h.insert(a3)
    h.mostrar()
    
    n = "davi"
    print(f"Buscando aluno {n}")
    n = h.busca(n)
    if n == None:
        print("Aluno não encontrado!")
    else:
        print(f"Aluno encontrado: {n}")
    
    print()

    n = "Daniel"
    print(f"Buscando aluno {n}")
    n = h.busca(n)
    if n == None:
        print("Aluno não encontrado!")
    else:
        print(f"Aluno encontrado: {n}")

# Executa a função main
main()