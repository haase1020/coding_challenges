# prompt: write a function that takes in an array of integers and returns a sorted
# version of that array. Use the bubble sort algorithm to sort the array.

# time complexity on average 0(n^2) / 0(1) space complexity

def bubbleSort(array):
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)
                isSorted = False
        counter += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


print(bubbleSort([8, 5, 2, 9, 5, 6, 3]))
