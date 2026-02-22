import sys
input = sys.stdin.readline

visited = [False] * 31  # 0은 안 씀, 1~30 사용

for _ in range(28):
    x = int(input())
    visited[x] = True

for i in range(1, 31):
    if not visited[i]:
        print(i)