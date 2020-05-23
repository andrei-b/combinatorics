def bracelets(s, n):
    if (n<4):
        yield s
    else:
        a = s.pop(n-1)
        for i in range(1, n):
            for s in bracelets(s, n-1):
                s.insert(i, a)
                yield s;
                s.pop(i)
        s.insert(n-1,a)
