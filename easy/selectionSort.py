# write a function that takes in an array of ints and returns a sorted version of that array.
# use the selection sort algorithm to sort the array

# time complexity 0(n^2) where n is length of input array/ space is 0(1)

def selectionSort(array):
    currentIdx = 0
    while currentIdx < len(array) - 1:
        smallestIdx = currentIdx
        for i in range(currentIdx + 1, len(array)):
            if array[smallestIdx] > array[i]:
                smallestIdx = i
        swap(currentIdx, smallestIdx, array)
        currentIdx += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


print(selectionSort([5, 4, 8, 7, 6, 9, 1, 2]))
