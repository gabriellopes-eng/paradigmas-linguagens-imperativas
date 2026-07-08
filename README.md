# Linguagens imperativas: um comparativo prático

Trabalho da disciplina de Paradigmas de Programação. A ideia é simples: pegar três
problemas clássicos de computação, implementar cada um em Python, Go e C#, e medir
como as três linguagens se comportam.

Não é um benchmark científico — os números variam de máquina para máquina e de execução
para execução. O objetivo é enxergar, na prática, as diferenças entre uma linguagem
interpretada (Python) e duas compiladas (Go e C#), além de comparar estilo de código e
organização.

## Os problemas

- **QuickSort** — ordenação recursiva por divisão e conquista. Roda sobre um vetor de
  5000 números aleatórios.
- **Torres de Hanói** — o quebra-cabeça recursivo, resolvido com 15 discos (32767
  movimentos).
- **Mochila (Knapsack)** — otimização por programação dinâmica, com capacidade 20 e
  10 itens.

Cada linguagem resolve os três e imprime uma tabela com o tempo de execução, o número
de linhas e o tamanho do arquivo de cada solução.

## Como rodar

Cada linguagem fica em sua própria pasta e roda de forma independente.

```bash
# Python 3
cd python
python main.py

# Go 1.26+
cd go
go run main.go

# C# / .NET 10
cd csharp
dotnet run
```

## Estrutura

```text
.
├── python/     main.py + sorting/ hanoi/ knapsack/
├── go/         main.go + sorting/ hanoi/ knapsack/
└── csharp/     Program.cs + Sorting/ Hanoi/ Knapsack/
```

A separação por pasta é proposital: cada problema mora em seu próprio módulo, e o
`main` de cada linguagem só orquestra a execução e a medição.

## O que a saída mostra

```text
==============================================================
COMPARATIVE METRICS - PYTHON
==============================================================
Problem             Time(s)        Lines     Size(KB)
------------------------------------------------------------
QuickSort           0.006665       64        1.37
Towers of Hanoi     0.327465       43        0.90
Knapsack            0.056076       63        1.80
==============================================================
```

Três colunas de métrica:

- **Tempo** — medido só em torno da chamada do algoritmo, sem contar setup nem I/O.
- **Linhas** — contagem do arquivo de cada solução, como proxy de verbosidade.
- **Tamanho** — o arquivo em KB.

Vale lembrar que Python paga o custo do interpretador e do overhead de inicialização, o
que costuma aparecer nos tempos. Go e C# passam por compilação antes de rodar, então a
comparação de tempo bruto não é uma disputa "justa" — e é exatamente esse contraste que
o trabalho quer mostrar.

## Autor

Gabriel Lopes de Albuquerque

Projeto acadêmico, sem fins comerciais.
