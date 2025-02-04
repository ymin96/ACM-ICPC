s = input()
one = int(s.count('1') / 2)
zero = int(s.count('0') / 2)
lst = []
for ch in s:
    lst.append(ch)
idx = 0
while one > 0:
    if lst[idx] == '1':
        del lst[idx]
        one -= 1
    else:
        idx += 1
idx = len(lst) - 1
while zero > 0:
    if lst[idx] == '0':
        del lst[idx]
        zero -= 1
    idx -= 1
for ch in lst:
    print(ch, end="")
