# ABC154a


def main():
    import sys
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    if s == u:
        a -= 1
    if t == u:
        b -= 1
    print(a, b)


if __name__ == '__main__':
    main()
