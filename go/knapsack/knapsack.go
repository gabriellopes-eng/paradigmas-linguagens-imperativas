package knapsack

func Solve(
	capacity int,
	weights []int,
	values []int,
) int {

	n := len(values)

	table := make([][]int, n+1)

	for i := range table {
		table[i] = make([]int, capacity+1)
	}

	for i := 1; i <= n; i++ {

		for currentCapacity := 0; currentCapacity <= capacity; currentCapacity++ {

			if weights[i-1] <= currentCapacity {

				includeItem :=
					values[i-1] +
						table[i-1][currentCapacity-weights[i-1]]

				excludeItem :=
					table[i-1][currentCapacity]

				if includeItem > excludeItem {

					table[i][currentCapacity] =
						includeItem

				} else {

					table[i][currentCapacity] =
						excludeItem
				}

			} else {

				table[i][currentCapacity] =
					table[i-1][currentCapacity]
			}
		}
	}

	return table[n][capacity]
}
