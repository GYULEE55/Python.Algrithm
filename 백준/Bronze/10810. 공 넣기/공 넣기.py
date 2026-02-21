N, M = map(int, input().split())
basket = [0] * (N+1)  # 0번 인덱스 무시, 1~N 사용
for _ in range(M):
    i, j, k = map(int, input().split())
    for x in range(i, j+1):   # i부터 j까지
        basket[x] = k
print(*basket[1:])  # 1번부터 출력

