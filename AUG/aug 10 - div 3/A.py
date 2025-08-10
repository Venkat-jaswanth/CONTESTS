import sys

readline = sys.stdin.readline
def solve():
    n = int(readline())
    a = list(map(int, readline().split()))
    b = list(map(int, readline().split()))
    pos_sum = 0
    for i in range(n):
        if a[i] > b[i]:
            pos_sum += a[i] - b[i]
    print(pos_sum + 1)
t = int(sys.stdin.readline())
for _ in range(t):
    solve()
