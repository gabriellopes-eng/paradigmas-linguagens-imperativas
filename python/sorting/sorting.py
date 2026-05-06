class QuickSort:

    @staticmethod
    def sort(array):
        QuickSort._quicksort(array, 0, len(array) - 1)
        return array

    @staticmethod
    def _quicksort(array, low, high):
        if low < high:
            pivot_index = QuickSort._partition(array, low, high)

            QuickSort._quicksort(array, low, pivot_index - 1)
            QuickSort._quicksort(array, pivot_index + 1, high)

    @staticmethod
    def _partition(array, low, high):
        pivot = array[high]
        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]

        array[i + 1], array[high] = array[high], array[i + 1]

        return i + 1
    
    