import math

t = int(input().strip())
for _ in range(t):
    n, k, p = map(int, input().split())
    ops = (abs(k) + p - 1) // p
    
    if ops <= n:
        print(ops)
    else:
        print(-1)
