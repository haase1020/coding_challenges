# write a function that takes in a string and groups anagrams together.


# not efficient or easy solution: time 0(WN log(N) + NW log(W)) and Space = 0(WN)
# W is number of words, N is length of longest word
def groupAnagrams(words):
    pass


# way simpler solution: sort, then put in hash table
print(groupAnagrams(["yo", "oy", "flop", "olfp", "act", "tac", "cat"]))
# expected outcome: [["yo", "oy"],["flop","olfp"],["act","tac","cat"]]
