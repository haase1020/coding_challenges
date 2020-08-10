# prompt: you are given an array of integers and an integer. Write a function that moves
# all instances for that integer in the array to the end of the array and returns the
# array. The function should perform this in place(i.e. it should mutate the input array),
# and doesn't need to maintain the order of the other integers.
#  time complexity: 0(n) where n is the length of the array. Space: 0(1) because nothing created


def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1
    while i < j:
        while i < j and array[j] == toMove:
            j -= 1
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        i += 1
    return array


# to test solution
print(moveElementToEnd([4, 1, 3, 2, 2, 2, 2, 2], 2))
# should return  [4,1,3,2,2,2,2,2]
