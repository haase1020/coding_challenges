def uncover_spy(n, trust):
    if len(trust) < n-1:
        return -1
    # initialize trust counts array with initial indices of count 0
    # use n+1 to make it easy to map each person to proper index in the array
    # for example, person 1 would map to index 1, person 2 to index 2, etc.
    trust_counts = [0] * (n + 1)

    for x, y in trust:
        trust_counts[x] -= 1  # could it also be "-="??? that works too....
        trust_counts[y] += 1

    # can start at 1 since first item in list doesn't mean anything (it's 0)
    for i in range(1, n + 1):
        if trust_counts[i] == n - 1:
            return i
    return -1


print(uncover_spy(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
