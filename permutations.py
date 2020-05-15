ddef permutes(s, n = len(n)):
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
    
    
def perm(a, k=0):
    if k == len(a):
        yield a
    else:
        for i in range(k, len(a)):
            a[k], a[i] = a[i], a[k]
            for s in perm(a, k + 1):
                yield s
            a[k], a[i] = a[i], a[k]