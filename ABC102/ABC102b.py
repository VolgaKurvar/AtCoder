# ABC102b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = input()
a = list(map(int, input().split()))
print(max(a)-min(a))
