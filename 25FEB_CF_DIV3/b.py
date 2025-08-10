t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    s = input().strip()
    D = s.count('-')
    U = s.count('_')
    if D < 2:
        print(0)
    else:
        left_dashes = D // 2
        right_dashes = (D + 1) // 2
        result = U * left_dashes * right_dashes
        print(result)