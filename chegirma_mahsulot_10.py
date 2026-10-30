n = int(input())
narxlar = list(map(int, input().split()))

qimmatlar = filter(lambda x: x >= 15000, narxlar)

chegirmali = list(map(lambda x: x - 3000, qimmatlar))


print(chegirmali)