# Imperative languages: a hands-on comparison

Project for the Programming Paradigms course. The idea is simple: take three classic
computer science problems, implement each one in Python, Go and C#, and measure how the
three languages behave.

This is not a scientific benchmark - the numbers vary from machine to machine and from
run to run. The goal is to see, in practice, the differences between an interpreted
language (Python) and two compiled ones (Go and C#), and to compare coding style and
organization along the way.

## The problems

- **QuickSort** - recursive divide-and-conquer sorting. Runs over an array of 5000
  random numbers.
- **Towers of Hanoi** - the recursive puzzle, solved with 15 disks (32767 moves).
- **Knapsack** - dynamic programming optimization, with capacity 20 and 10 items.

Each language solves all three and prints a table with the execution time, line count
and file size of each solution.

## How to run

Each language lives in its own folder and runs independently.

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

## Structure

```text
.
├── python/     main.py + sorting/ hanoi/ knapsack/
├── go/         main.go + sorting/ hanoi/ knapsack/
└── csharp/     Program.cs + Sorting/ Hanoi/ Knapsack/
```

The folder split is intentional: each problem lives in its own module, and the `main`
of each language only orchestrates the run and the measurement.

## What the output shows

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

Three metric columns:

- **Time** - measured only around the algorithm call, without setup or I/O.
- **Lines** - line count of each solution file, used as a proxy for verbosity.
- **Size** - the file in KB.

Keep in mind that Python pays the cost of the interpreter and the startup overhead,
which usually shows up in the timings. Go and C# go through compilation before running,
so a raw time comparison is not a "fair" fight - and that contrast is exactly what this
project is meant to show.

## Author

Gabriel Lopes de Albuquerque

Academic project, no commercial purpose.
