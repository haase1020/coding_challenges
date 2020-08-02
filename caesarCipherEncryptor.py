# prompt: given a non-empty string of lowercase letters and a non-negative integer representing
# a key, write a function that returns a new string obtained by shifting every letter in the input
# string by k positions in the alphabet, where k is the key.
# note that letters should "wrap" around the alphabet; in other words, the letter z
# shifted by 1 returns the letter a.
# assuming alphabet only and lower case
# use inicode value

# #Solution 1
# # 0(n) time complexity space 0(n)
# def caesarCipherEncryptor(string, key):
#     newLetters = []
#     newKey = key % 26
#     for Letter in string:
#         newLetters.append(getNewLetter(Letter, newKey))
#     return "".join(newLetters)


# def getNewLetter(Letter, key):
#     newLetterCode = ord(Letter) + key
#     return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)


# Solution 2
# 0(n) time and 0(n) space
def caesarCipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    for Letter in string:
        newLetters.append(getNewLetter(Letter, newKey, alphabet))
    return "".join(newLetters)


def getNewLetter(Letter, key, alphabet):
    newLetterCode = alphabet.index(Letter) + key
    return alphabet[newLetterCode] if newLetterCode <= 25 else alphabet[newLetterCode % 26]


# to test code:
print(caesarCipherEncryptor('zfc', 2))
# expect result: 'bhe'
