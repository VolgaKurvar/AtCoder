# ABC165e

def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    #再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))
    
    n, m = map(int, input().split())
    
    
if __name__ == '__main__':
    main()
