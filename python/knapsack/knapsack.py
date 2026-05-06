class Knapsack:

    @staticmethod
    def solve(capacity, weights, values):

        n = len(values)

        table = []

        for _ in range(n + 1):
            row = [0] * (capacity + 1)
            table.append(row)

        for i in range(1, n + 1):

            for current_capacity in range(capacity + 1):

                if weights[i - 1] <= current_capacity:

                    include_item = (
                        values[i - 1]
                        + table[i - 1][
                            current_capacity - weights[i - 1]
                        ]
                    )

                    exclude_item = table[i - 1][current_capacity]

                    table[i][current_capacity] = max(
                        include_item,
                        exclude_item
                    )

                else:

                    table[i][current_capacity] = table[i - 1][
                        current_capacity
                    ]

        return table[n][capacity]