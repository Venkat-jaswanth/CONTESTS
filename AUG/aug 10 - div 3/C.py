import sys
from collections import Counter
readline = sys.stdin.readline
def solve():
        n, k = map(int, readline().split())
        s_list = list(map(int, readline().split()))
        t_list = list(map(int, readline().split()))

        def get_class_representative(x, k_val):
            remainder = x % k_val
            return min(remainder, (k_val - remainder) % k_val)

        s_classes = Counter(get_class_representative(x, k) for x in s_list)

        t_classes = Counter(get_class_representative(x, k) for x in t_list)

        if s_classes == t_classes:
            print("YES")
        else:
            print("NO")


def main():
        num_test_cases = int(readline())
        for _ in range(num_test_cases):
            solve()


if __name__ == "__main__":
    main()