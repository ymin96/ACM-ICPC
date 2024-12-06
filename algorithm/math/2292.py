N = int(input())
cnt = 1
a = 1
b = 6
while a < N:
    a += b
    b += 6
    cnt += 1
print(cnt)