using System.Diagnostics;

using SortingNamespace;
using HanoiNamespace;
using KnapsackNamespace;

class Program
{
    static int CountLines(string path)
    {
        return File.ReadAllLines(path).Length;
    }

    static double FileSize(string path)
    {
        return new FileInfo(path).Length / 1024.0;
    }

    static void Main()
    {
        Random random = new Random();

        // QUICKSORT
        int[] numbers =
            Enumerable.Range(1, 50000)
            .OrderBy(x => random.Next())
            .ToArray();

        Stopwatch stopwatch =
            Stopwatch.StartNew();

        QuickSort.Sort(numbers);

        stopwatch.Stop();

        double quicksortTime =
            stopwatch.Elapsed.TotalSeconds;

        // HANOI
        List<string> moves = new();

        stopwatch.Restart();

        Hanoi.Solve(
            20,
            "A",
            "B",
            "C",
            moves
        );

        stopwatch.Stop();

        double hanoiTime =
            stopwatch.Elapsed.TotalSeconds;

        // KNAPSACK
        int[] weights =
        {
            2, 5, 7, 3, 1,
            4, 6, 8, 9, 2
        };

        int[] values =
        {
            10, 4, 8, 5, 3,
            7, 6, 9, 2, 1
        };

        stopwatch.Restart();

        for (int i = 0; i < 10000; i++)
        {
            Knapsack.Solve(
                20,
                weights,
                values
            );
        }

        stopwatch.Stop();

        double knapsackTime =
            stopwatch.Elapsed.TotalSeconds;

        // # TABELA DE MÉTRICAS
        Console.WriteLine(
            "\n=============================================================="
        );

        Console.WriteLine(
            "MÉTRICAS COMPARATIVAS - C#"
        );

        Console.WriteLine(
            "=============================================================="
        );

        Console.WriteLine(
            $"{"Problema",-20}" +
            $"{"Tempo(s)",-15}" +
            $"{"Linhas",-10}" +
            $"{"Tamanho(KB)",-15}"
        );

        Console.WriteLine(
            "------------------------------------------------------------"
        );

        Console.WriteLine(
            $"{"QuickSort",-20}" +
            $"{quicksortTime,-15:F6}" +
            $"{CountLines("Sorting/Sorting.cs"),-10}" +
            $"{FileSize("Sorting/Sorting.cs"),-15:F2}"
        );

        Console.WriteLine(
            $"{"Torres de Hanoi",-20}" +
            $"{hanoiTime,-15:F6}" +
            $"{CountLines("Hanoi/Hanoi.cs"),-10}" +
            $"{FileSize("Hanoi/Hanoi.cs"),-15:F2}"
        );

        Console.WriteLine(
            $"{"Mochila",-20}" +
            $"{knapsackTime,-15:F6}" +
            $"{CountLines("Knapsack/Knapsack.cs"),-10}" +
            $"{FileSize("Knapsack/Knapsack.cs"),-15:F2}"
        );

        Console.WriteLine(
            "============================================================"
        );
    }
}