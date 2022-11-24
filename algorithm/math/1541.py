temp = input()
a = temp.split("-")
ans = sum(map(int, a[0].split("+")))
for i in range(1, len(a)):
    ans -= sum(map(int, a[i].split("+")))
print(ans)