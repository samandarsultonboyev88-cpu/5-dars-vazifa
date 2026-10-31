def ijobiy_yigindi(*sonlar):
    yigindi = 0
    for x in sonlar:
       if x > 0:
           yigindi += x
    return yigindi
    

n = int(input())

sonlar = list(map(int, input().split()))  

print(ijobiy_yigindi(*sonlar))