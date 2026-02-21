N = int(input())
arr = list(map(int, input().split()))  # N개 수 한줄에 입력
v = int(input())                        # 찾을 수

print(arr.count(v))                     # v 개수 출력
