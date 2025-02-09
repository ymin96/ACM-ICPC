import sys

N = int(sys.stdin.readline().strip())
lst = sys.stdin.readline().strip()
lst = list(lst)
answer = N


def ball(lst):
    red = 0
    blue = 0
    red_check = False
    blue_check = False

    for i in range(N):
        if lst[i] == 'B':
            red_check = True
        if lst[i] == 'R':
            blue_check = True
        if red_check and lst[i] == 'R':
            red += 1
        if blue_check and lst[i] == 'B':
            blue += 1
    return min(red, blue)


answer = min(answer, ball(lst))
lst.reverse()
answer = min(answer, ball(lst))

print(answer)
