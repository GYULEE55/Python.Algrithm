import sys
input=sys.stdin.readline
now = list(map(int, input().split()))
need=[1,1,2,2,2,8]
ans = [need[i] - now[i] for i in range(6)]
print(*ans)
  

 