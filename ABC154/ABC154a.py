# ABC154a


def main():
    import sys
    sys.setrecursionlimit(10**6)
    # �ċA�֐����g��Ȃ�����Pypy�ŏo������

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
