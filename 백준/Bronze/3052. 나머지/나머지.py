mods=set()
for _ in range(10):
    n= int(input())
    mods.add(n%42)
print(len(mods))