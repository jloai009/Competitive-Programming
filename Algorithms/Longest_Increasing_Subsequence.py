def bisect_left(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = left+(right-left)//2
        if array[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1

    return right + 1

def longestIncreasingSubsequence(array):
    prev = [None] * len(array)

    IS_values = [float("-inf")]
    IS_indexes = [None]

    for i in range(len(array)):
        if array[i] > IS_values[-1]:
            prev[i] = IS_indexes[-1]
            IS_values.append(array[i])
            IS_indexes.append(i)
        else:
            k = bisect_left(IS_values, array[i])
            IS_values[k] = array[i]
            IS_indexes[k] = i
            prev[i] = IS_indexes[k-1]

    ptr = IS_indexes[-1]
    answer = []

    while ptr != None:
        answer.append(array[ptr])
        ptr = prev[ptr]

    answer.reverse()
    return answer
