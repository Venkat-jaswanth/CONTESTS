import sys
def main():
    b = sys.stdin.read().split()
    a = int(b[0])
    c = 1
    o = []
    for _ in range(a):
        d = int(b[c]); c += 1
        e = list(map(int, b[c:c+d])); c += d
        f = 0
        g = 1
        h = 1
        for i in range(d):
            k = 0
            for j in range(i+1, d):
                if e[j] > e[i]:
                    k += 1
                elif e[j] < e[i]:
                    k -= 1
                if k < f:
                    f = k
                    g = i + 1
                    h = j + 1
        o.append(f"{g} {h}")
    sys.stdout.write("\n".join(o))
main()
