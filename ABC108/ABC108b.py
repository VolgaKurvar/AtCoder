# ABC108b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

x1, y1, x2, y2 = map(int, input().split())
x3 = x2 - (y2 - y1)
y3 = y2 + (x2 - x1)
x4 = x1 - (y2 - y1)
y4 = y1 + (x2 - x1)
print(x3, y3, x4, y4)
