# prompt: write a function that takes in an array of integers and returns a sorted version
# of that array. Use the insertion sort algorithm to sort the array.

# this type of insertion is easy to understand and implement
# time complexity on avg. is 0(n^2) where n is the length of input array, space complexity is 0(1)

def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(j, j - 1, array)
            j -= 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


print(insertionSort([5, 4, 7, 6, 9]))
