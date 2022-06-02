
def quickSort(array):

    def partition(left, right):
        pivot_index = random.randint(left, right)
        array[pivot_index], array[right] = array[right], array[pivot_index]
        pivot = array[right]
        ptr = left
        for i in range(left, right):
            if array[i] < pivot:
                array[ptr], array[i] = array[i], array[ptr]
                ptr += 1
        
        array[ptr], array[right] = array[right], array[ptr]
        return ptr

    def qs(left, right):
        if right-left > 0:
            pivot_index = partition(left, right)
            qs(left, pivot_index-1)
            qs(pivot_index+1, right)

    qs(0, len(array)-1)

    return array
