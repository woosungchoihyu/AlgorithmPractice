n = 1260
cnt = 0

coin_types = [500, 100, 50, 10]

for i in coin_types:
    cnt += n // i
    n = n % i

print(cnt)