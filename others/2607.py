import copy

n=int(input())
count=0
lst=[[0]*26 for i in range(n)]
for i in range(0,n):
    ch = input()
    for j in ch:
        lst[i][ord(j)-65]=lst[i][ord(j)-65]+1

for i in range(1,n):
    if lst[0]==lst[i]:
        count=count+1
    elif abs(sum(lst[0])-sum(lst[i]))==1:
        check=0
        for j in range(26):
            if lst[0][j] != lst[i][j]:
                check=check+1
        if check==1:
            count=count+1
    elif sum(lst[0])==sum(lst[i]):
        check=0
        for j in range(26):
            if lst[0][j] != lst[i][j]:
                check=check+1
        if check==2:
            count=count+1

print(count)