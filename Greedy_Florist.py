def getMinimumCost(k, c):
    cost = 0
    n = 1
    c = sorted(c)
    cinit = c

    while k <= len(c):
        cost += sum(c[len(c) - k:])
        n += 1
        c = [x * n for x in cinit[:len(cinit) - (n - 1) * k]]
    cost += sum(c)

    return cost