import sys
from collections import Counter
input = sys.stdin.readline

word = input().strip().upper()
cnt = Counter(word)

mx = max(cnt.values())
top = [ch for ch, v in cnt.items() if v == mx]

print(top[0] if len(top) == 1 else "?")