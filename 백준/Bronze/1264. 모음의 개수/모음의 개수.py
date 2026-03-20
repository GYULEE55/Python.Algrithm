import sys
input = sys.stdin.readline
while True:
    s = input().rstrip("\n")
    if s == "#":
        break
    print(len([ch for ch in s if ch.lower() in "aeiou"]))