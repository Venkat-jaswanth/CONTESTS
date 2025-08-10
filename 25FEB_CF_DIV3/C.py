import sys
def main():
    s = sys.stdin.read().split()
    a = int(s[0])
    i = 1
    o = []
    m = (1 << 32) - 1
    def f(x):
        k = 0
        while (1 << k) < x:
            k += 1
        return k
    for _ in range(a):
        b = int(s[i]); i += 1
        c = int(s[i]); i += 1
        if b == 1:
            o.append(str(c))
            continue
        e = 0
        while e <= b:
            if (e & ((~c) & m)) != 0:
                break
            e += 1
        d = e if e < b else b
        g = f(d)
        h = (1 << g) - 1
        j = (h == c)
        if j:
            k = d
        else:
            k = e if e < (b - 1) else (b - 1)
        l = []
        for x in range(k):
            l.append(x)
        if not j:
            l.append(c)
        while len(l) < b:
            l.append(0)
        o.append(" ".join(map(str, l)))
    sys.stdout.write("\n".join(o))
main()


