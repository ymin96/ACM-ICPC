def preOrder(root):
    global tree
    if root == ".":
        return
    print(root, end="")
    left, right = tree[root]
    preOrder(left)
    preOrder(right)

def inOrder(root):
    global tree
    if root == ".":
        return
    left, right = tree[root]
    inOrder(left)
    print(root, end="")
    inOrder(right)

def postOrder(root):
    global tree
    if root == ".":
        return
    left, right = tree[root]
    postOrder(left)
    postOrder(right)
    print(root, end="")

global tree
tree = {}
n = int(input())
for i in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]
preOrder("A")
print()
inOrder("A")
print()
postOrder("A")