import sys

# T = int(input())

# for i in range(T):
#     A, B = map(int, input().split())
#     print("Case #%d: %d + %d = %d" % (i + 1, A, B, A + B))

T = int(sys.stdin.readline())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print("Case #%d: %d + %d = %d" % (i + 1, A, B, A + B))