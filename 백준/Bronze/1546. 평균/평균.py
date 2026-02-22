import sys
input = sys.stdin.readline

N = int(input())
scores = list(map(int, input().split()))

M = max(scores)
new_avg = sum(score / M * 100 for score in scores) / N

print(new_avg)