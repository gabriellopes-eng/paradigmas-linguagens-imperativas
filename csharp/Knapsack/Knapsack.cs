namespace KnapsackNamespace
{
    public class Knapsack
    {
        public static int Solve(
            int capacity,
            int[] weights,
            int[] values
        )
        {
            int n = values.Length;

            int[,] table =
                new int[n + 1, capacity + 1];

            for (int i = 1; i <= n; i++)
            {
                for (
                    int currentCapacity = 0;
                    currentCapacity <= capacity;
                    currentCapacity++
                )
                {
                    if (
                        weights[i - 1]
                        <= currentCapacity
                    )
                    {
                        int includeItem =
                            values[i - 1]
                            + table[
                                i - 1,
                                currentCapacity
                                - weights[i - 1]
                            ];

                        int excludeItem =
                            table[
                                i - 1,
                                currentCapacity
                            ];

                        table[i, currentCapacity] =
                            Math.Max(
                                includeItem,
                                excludeItem
                            );
                    }
                    else
                    {
                        table[i, currentCapacity] =
                            table[
                                i - 1,
                                currentCapacity
                            ];
                    }
                }
            }

            return table[n, capacity];
        }
    }
}