def ijobiy_yigindi(*sonlar):
    musbatlar = [x for x in sonlar if x > 0]
    return sum(musbatlar) if musbatlar else 0

n = int(input())

sonlar = list(map(int, input().split()))

print(ijobiy_yigindi(*sonlar))