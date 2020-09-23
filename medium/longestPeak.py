# write a function that takes in an array of integers and returns the length of the loongest in in the array.
# a peak is deffined as adjeacent integers in the array that are strictly increasing until they reach a tip (the highest value in the peak)
# at which point they become strictly decreasing. At least three integers are required to form a peak
# for example, inte integers 1,4,10,2 form a peak, but 4,0,10 don't, 1,2,2,0 don't, 1,2,3 don't

#             len:3 | len:6
# ex: [1,2,3,|3,4,0,|10,6,5,-1,-3,|2,3]
#               p    p


# 0(n) time | 0(1) space
def longestPeak(array):
    longestPeakLength = 0
    i = 1
    while i < len(array) - 1:
        isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if not isPeak:
            i += 1
            continue

        leftIdx = i - 2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -= 1
        rightIdx = i + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1

        currentPeakLength = rightIdx - leftIdx - 1
        longestPeakLength = max(longestPeakLength, currentPeakLength)
        i = rightIdx
    return longestPeakLength


print(longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))  # expected = 6
