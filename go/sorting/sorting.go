package sorting

func QuickSort(array []int) []int {

	quicksort(array, 0, len(array)-1)

	return array
}

func quicksort(array []int, low int, high int) {

	if low < high {

		pivotIndex := partition(array, low, high)

		quicksort(array, low, pivotIndex-1)

		quicksort(array, pivotIndex+1, high)
	}
}

func partition(array []int, low int, high int) int {

	pivot := array[high]

	i := low - 1

	for j := low; j < high; j++ {

		if array[j] <= pivot {

			i++

			array[i], array[j] = array[j], array[i]
		}
	}

	array[i+1], array[high] = array[high], array[i+1]

	return i + 1
}
