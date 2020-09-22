# write a function that takes in an n x m two dimenstional array (that can be square-shaped when n==m) and returns
# a one-dminesional array of all the array's elements in spiral order.
# Spiral order starts at the top left corner of the two dimentional array, goes to the right, and process in a spiral pattern all the way
# until every element has been visited.


# 0(n) time | 0(n) space/ or constant space
# iterative solution

# def spiralTraverse(array):

#     result = []
#     startRow, endRow = 0, len(array) - 1
#     startCol, endCol = 0, len(array[0]) - 1

#     while startRow <= endRow and startCol <= endCol:
#         if startRow == endRow:
#             break  # avoid double-counting single row
#         for col in range(startCol, endCol + 1):
#             result.append(array[startRow][col])
#         for row in range(startRow + 1, endRow + 1):
#             result.append(array[row][endCol])

#         for col in reversed(range(startCol, endCol)):
#             result.append(array[endRow][col])
#         for row in reversed(range(startRow + 1, endRow)):
#             result.append(array[row][startCol])

#         startRow += 1
#         endRow -= 1
#         startCol += 1
#         endCol -= 1

#     return result


# 0(n) time | 0(n) space
def spiralTraverse(array):
    result = []
    spiralFill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)
    return result


def spiralFill(array, startRow, endRow, startCol, endCol, result):
    if startRow > endRow or startCol > endCol:
        return
    for col in range(startCol, endCol + 1):
        result.append(array[startRow][col])
    for row in range(startRow + 1, endRow + 1)
    result.append(array[row][endCol])

    for col in reversed(range(startCol, endCol)):
        result.append(array[endRow][col])
    for row in reversed(range(startRow + 1, endRow)):
        result.append(array[row][startCol])

    spiralFill(array, startRow + 1, endRow - 1,
               startCol + 1, endCol - 1, result)
