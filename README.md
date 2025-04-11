# Tabela Hash com Encadeamento Duplo

## 📄 Descriçãd
Implementação da estrutura de dados tabela hash com encadeamento Duplo em python.

---

## Lógica

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
