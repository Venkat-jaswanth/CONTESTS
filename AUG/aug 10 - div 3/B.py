import sys
readline = sys.stdin.readline


def solve():
    n = int(readline())
    result = []
    for i in range(n):
        if i % 2 == 0: 
            result.append(-1)
        else:          
            result.append(3)

    if n % 2 == 0:
        result[n - 1] = 2
    
    print(*result)


def main():
        t = int(readline())
        for _ in range(t):
            solve()


if __name__ == "__main__":
    main()