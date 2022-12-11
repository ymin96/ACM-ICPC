import sys

sys.setrecursionlimit(10 ** 5)

def tree(first, last, root):
    global preOrder, inOrder, postOrder
    preOrder.append(postOrder[root])
    mid = inOrder.index(postOrder[root])
    left = mid - first
    right = last - mid
    if left > 0:
        tree(first, mid - 1, root - right - 1)
    if right > 0:
        tree(mid + 1, last, root - 1)

global preOrder, inOrder, postOrder
n = int(input())
inOrder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))
preOrder = []
tree(0, n - 1, n - 1)

for item in preOrder:
    print(item, end=" ")
