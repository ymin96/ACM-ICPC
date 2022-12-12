def prec(op):
    if op == '(' or op == ')':
        return 0
    elif op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    else:
        return -1


def infix_to_postfix(exp):
    answer = ''
    lst = []
    for ch in exp:
        if ch == '+' or ch == '-' or ch == '*' or ch == '/':
            while lst != [] and (prec(ch) <= prec(lst[-1])):
                answer += lst.pop()
            lst.append(ch)
        elif ch == '(':
            lst.append(ch)
        elif ch == ')':
            top = lst.pop()
            while top != '(':
                answer += top
                top = lst.pop()
        else:
            answer += ch
    while lst:
        answer += lst.pop()
    return answer


n = input()
print(infix_to_postfix(n))
