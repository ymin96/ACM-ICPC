import math

mn,mx=map(int,input().split())

lst=[1 for _ in range(1000001)]
sosu=[]
result=[1 for i in range(mn,mx+1)]
for i in range(2,1000001):
    if lst[i]==1:
        sosu.append(i*i)
        for j in range(i*2,1000001,i):
            lst[j]=0
count=0
t_mx=int(math.sqrt(mx))
for i in sosu:
    if i > mx:
        break
    temp=int(mn/i)
    for j in range(temp*i,mx+1,i):
        if mn<=j and j<=mx:
            result[j-mn]=0

for i in result:
    if i != 0:
        count=count+1

print(count)
#print(result)