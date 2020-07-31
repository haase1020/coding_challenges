# coding challenge problem for unit assessment
# from CodeSignal
# prompt: in a city-state of n people, there is a rumor going
# around that one of the n people is a spy for the neighboring
# city state. The spy, if it exits:
# 1. does not trust anyone
# 2. is trusted by everyone else
# 3. works alone ( not other spies)
# you are given a list of pairs, gtus. Each trust[i] = [a,b]
# represent the fact that the person a trusts person b.
# if the spy exists and can be found, return their identifier.
# otherwise return -1


# outdegree of vertex (person) is # of directed edges going towards it. how many people trust person
# indegree: of vertex (person) is # of directed edges going into it. # people trusted by that person
# spy: outdgree of 0 and indegree of n-1 (everyone trusts them except the spy)
# return: identifier if spy found, else -1

def uncover_spy(n, trust):
    if len(trust) < n-1:
        return -1

    indegree = [0] * (n + 1)
    outdegree = [0] * (n + 1)

    for x, y in trust:
        outdegree[x] += 1
        indegree[y] += 1

    for i in range(1, n + 1):
        if indegree[i] == n - 1 and outdegree[i] == 0:
            return i
    return -1
