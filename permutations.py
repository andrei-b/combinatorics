def rshift(s, n):
    t = s[n-1]
    s.remove(t)
    s.insert(0, t)
    return s


def permutations(s, n):
    for i in range(n):
        if (n > 1):
            for s in permutations(s, n - 1):
                yield s
            s = rshift(s, n)
        else:
            yield s


for s in permutations([1,2,3,4],4):
    print(s)
