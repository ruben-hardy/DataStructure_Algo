class SortingAlgorithms:
    """
    Class contains Top 4 sorting algorithms that I know of
    """

    def __init__(self, sequence):
        self.sequence = sequence
        self.seq_length = len(self.sequence)-1

    def BubbleSort(self):
        sorted = False
        
        while not sorted:
            sorted = True
            for i in range(self.seq_length):
                if self.sequence[i] > self.sequence[i+1]:
                    self.sequence[i], self.sequence[i+1] = self.sequence[i+1], self.sequence[i]
                    sorted = False
        return self.sequence

    def SelectionSort(self):
        for i in range(self.seq_length):
            min_value = i
            for j in range(i+1, len(self.sequence)):
                if self.sequence[j] < self.sequence[i]:
                    min_value = j
            if min_value != i:
                self.sequence[min_value], self.sequence[i] = self.sequence[i], self.sequence[min_value]
        return self.sequence

    def InsertionSort(self):
        for i in range(1, len(self.sequence)):
            while self.sequence[i] < self.sequence[i-1] and i > 0:
                self.sequence[i-1], self.sequence[i] = self.sequence[i], self.sequence[i-1]
                i -= 1
        return self.sequence

    def QuickSort(self, seq):
        if len(seq) < 2:
            return seq
        pivot = seq[-1]
        left_array = list()
        right_array = list()      
        for i in range(len(seq)-1):
            if seq[i] > pivot:
                right_array.append(seq[i])
            else:
                left_array.append(seq[i])
        return self.QuickSort(left_array) + [pivot] + self.QuickSort(right_array)

    
                     
lst = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
run = SortingAlgorithms(lst)
print(f'Unsorted list { lst }')
print(f'Bubble Sort { run.BubbleSort() }')
print(f'Selection Sort { run.SelectionSort() }')
print(f'Insertion Sort { run.InsertionSort() }')
print(f'Quick Sort { run.QuickSort(lst) }')

