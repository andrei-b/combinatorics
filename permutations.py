ddef permutes(s, n):
    for i in range(n):
        if (n > 1):
            for s in permutes(s, n - 1):
                yield s
            s.insert(0, s[n-1])
            s.pop(n)
        else:
            yield s


for s in permutations([1,2,3,4],4):
    print(s)
