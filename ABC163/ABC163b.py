# ABC163b


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = sum(a)
    print(max(-1, n-a))


if __name__ == '__main__':
    main()
