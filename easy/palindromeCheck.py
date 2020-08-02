# prompt: write a function that takes in a non-empty string and that returns a boolean
# representing whether that string is a palindrome.
# a palindrome is a string that is written the same forward and backward. Single character
# strings are palindromes.

# # space complexity 0(n) and time complexity 0(n^2)

# def isPalindrome(string):
#     reversedString = ""
#     for i in reversed(range(len(string))):
#         reversedString += string[i]
#     return string == reversedString


# # 0(n) time and 0(n) space:
# def isPalindrome(string):
#     reversedChars = []
#     for i in reversed(range(len(string))):
#         reversedChars.append(string[i])
#     return string == "".join(reversedChars)


# # recursive: 0(n) time and space
# def isPalindrome(string, i = 0):
#     j = len(string) - 1 - i
#     return True if i >= j else string[i] ==string[j] and isPalindrome(string, i + 1)


# # tail recursion: still 0(n) time and likely space
# def isPalindrome(string, i=0):
#     j = len(string) - 1 - i
#     if i > j:
#         return True
#     if string[i] != string[j]:
#         return False
#     return isPalindrome(string, i + 1)

# iterative case - has best time and space complexity 0(n) time 0(1) space


def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True


print(isPalindrome('abccba'))
