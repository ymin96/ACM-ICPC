end=int(input())
start=1
lst=[0 for _ in range(10)]
temp=1

def calc(n,temp):
    global lst
    while n>0:
        lst[n%10]=lst[n%10]+(1*temp)
        n=int(n/10)
if end == 1:
    lst[1]=1
else:
    while True:
        while start%10 != 0 and end != start:
            calc(start,temp)
            start=start+1
    
        if start == end:
           calc(start,temp)
           break

        while end%10 != 9 and end != start:
            calc(end,temp)
            end = end - 1

        if start == end:
            calc(end,temp)
            break

        x=(int(end/10))-(int(start/10))+1
        for i in range(10):
            lst[i]=lst[i]+(x*temp)
        temp=temp*10
        end=int(end/10)
        start=int(start/10)
for i in lst:
    print(i,end=' ')
