# given two non-empty array of integers, write a function that determines whether
# the 2nd array is a susequence of the first one.

# # solution 1 is a while loop
# def isValidSubsequence(array, sequence):
#     arrIdx = 0
#     seqIdx = 0
#     while arrIdx < len(array) and seqIdx < len(sequence):
#         if array[arrIdx] == sequence[seqIdx]:
#             seqIdx += 1
#         arrIdx += 1
#     return seqIdx == len(sequence)


# solution 2 is a for loop
def isValidSubsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)


print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
