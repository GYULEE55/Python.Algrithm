while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break        # 0 0 이면 종료
    print(A+B)