max_x=0
max_r=0
for i in range(1,10):
    x= int(input())
    if max_x<x:
        max_x=x
        max_r=i
print(max_x)
print(max_r)