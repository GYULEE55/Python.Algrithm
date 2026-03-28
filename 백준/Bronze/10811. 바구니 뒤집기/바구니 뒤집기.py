import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(range(1, N + 1))  # [1,2,3,...,N]

for _ in range(M):
    i, j = map(int, input().split())
    # i, j는 1-index라서 파이썬 0-index로 맞추려면 i-1, j
    arr[i-1:j] = reversed(arr[i-1:j])

print(*arr)
