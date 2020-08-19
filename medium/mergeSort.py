def mergeSort(array):
    pass


# recursive visual
[8, 5, 2, 9, 5, 6, 3]
[8, 5, 2, 9][5, 6, 3]
# go down left side first, then right
[8, 5][2, 9]
[8][5]

[5, 8][2, 9]
[2, 5, 8, 9]

# then right side
[5, 6][3]
[5][6][3]
# now sort
[5, 6][3]
[3, 5, 6]

now two arrays:
[2, 5, 8, 9][3, 5, 6]
then compare starting at left of each item in array
[2, 3, 5, 5, 6, 8, 9]  # final outcome
# base case is when arrays are length of 1
# time complexity: will ALWAYS be 0(n log(n))
# space complexity: 0(n log(n))


# better option visual
[8, 5, 2, 9, 5, 6, 3]  # main array m
[8, 5, 2, 9, 5, 6, 3]  # auxiliary array a
# then they end up switching order
[8, 5, 2, 9]  # a
[8, 5, 2, 9]  # m
[8, 5]  # m
[8, 5]  # a
[8][5]  # helper
# then call doMerge method passing in [8][5]
