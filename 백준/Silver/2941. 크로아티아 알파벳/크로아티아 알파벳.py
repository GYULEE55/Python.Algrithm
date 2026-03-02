# Baekjoon 2941 - 크로아티아 알파벳
s = input().strip()

cro = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]

for pat in cro:
    s = s.replace(pat, "*")  # 한 글자로 치환

print(len(s))