# Tabela Hash com Encadeamento Duplo

## 📄 Descrição
Implementação da estrutura de dados tabela hash com encadeamento Duplo em python. Já vem acompanhado de teste no arquivo main.

---

## 🧠 Lógica

O sistema possui dois níveis de hash, onde ambos os níveis utilizam funções hash diferentes para mapear os elementos:

### Nível 1
- Vetor de tamanho fixo com 10 posições.

- Cada posição aponta para uma tabela hash secundária.

### Nível 2
- Cada tabela do segundo nível é composta por um vetor de tamanho n/10.

- Cada posição desse vetor contém uma lista.

- A função hash do segundo nível é diferente da do primeiro.

---

## 🗂️ Arquivos
- _pycache_: Contém o arquivo executável;
  
- maze.py: Arquivo principal;
  
- aluno.py: Contém a implementação do objeto aluno;
  
- tabela_hash.py: Contém a implementação da tabela hash.

---

## ⚙️ Execução do código

```
python main.py
```
---

## 🖥️ Simulação
 ```
        Tabela hash de alunos
[0][0] ->
[0][1] ->
[0][2] ->
[1][0] ->
[1][1] ->
[1][2] ->
[2][0] ->
[2][1] ->
        Nome: Daniel     Nota: 8
[2][2] ->
[3][0] ->
        Nome: Davi       Nota: 9
[3][1] ->
[3][2] ->
[4][0] ->
[4][1] ->
[4][2] ->
[5][0] ->
[5][1] ->
[5][2] ->
[6][0] ->
[6][1] ->
[6][2] ->
[7][0] ->
[7][1] ->
[7][2] ->
[8][0] ->
[8][1] ->
[8][2] ->
[9][0] ->
[9][1] ->
        Nome: Maria      Nota: 7
[9][2] ->

Buscando aluno davi
Aluno não encontrado!

Buscando aluno Daniel
Aluno encontrado: Nome: Daniel   Nota: 8

```
