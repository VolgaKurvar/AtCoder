# ABC155e


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    n = input()[:-1]
    ans = 0
    before = False
    for i in n:
        num = int(i)
        if num < 11 - num:
            ans += num
            before = False
        else:
            ans += 11 - num
            if before:
                ans -= 1
            before = True
    print(ans)


if __name__ == '__main__':
    main()
