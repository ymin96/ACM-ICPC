N = int(input())
lst = []
for i in range(N):
    lst.append(input())
kbs1 = lst.index("KBS1")
kbs2 = lst.index("KBS2")
ans = ""
ans += "1"*kbs2
ans += "4"*kbs2
if kbs2 > kbs1:
    ans += "1"
ans += "1"*kbs1
if kbs2 > kbs1:
    ans += "4"
ans += "4"*kbs1
print(ans)