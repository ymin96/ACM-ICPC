while True:
    lst = list(map(int, input().split()))
    lst.sort()
    if lst[0] == 0 and lst[1] == 0 and lst[2] == 0:
        break
    elif lst[2] >= (lst[0] + lst[1]):
        print("Invalid")
    elif lst[0] != lst[1] != lst[2]:
        print("Scalene")
    elif lst[0] == lst[1] == lst[2]:
        print("Equilateral")
    else:
        print("Isosceles")