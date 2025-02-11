import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = Node("")
        self.cursor = self.head
        self.length = 0

    def append(self, data):
        node = Node(data)
        if self.cursor is self.head and self.length == 0:
            self.head.next = node
            node.prev = self.head
            self.cursor = node
        elif self.cursor.next is None:
            node.prev = self.cursor
            self.cursor.next = node
            self.cursor = node
        else:
            if self.cursor is self.head:
                node.next = self.cursor.next
                node.prev = self.head
                self.cursor.next.prev = node
                self.cursor.next = node
                self.cursor = node
            else:
                node.prev = self.cursor
                node.next = self.cursor.next
                self.cursor.next.prev = node
                self.cursor.next = node
                self.cursor = node
        self.length += 1

    def left(self):
        if self.cursor.prev is not None:
            self.cursor = self.cursor.prev

    def right(self):
        if self.cursor.next is not None:
            self.cursor = self.cursor.next

    def delete(self):
        if self.length > 1 and self.cursor is not self.head and self.cursor.prev is not None:
            if self.cursor.next is not None:
                self.cursor.prev.next = self.cursor.next
                self.cursor.next.prev = self.cursor.prev
                self.cursor = self.cursor.prev
            else:
                self.cursor = self.cursor.prev
                self.cursor.next = None
            self.length -= 1

    def print(self):
        node = self.head
        while node is not None:
            print(node.data, end="")
            node = node.next


lst = sys.stdin.readline().strip()
N = int(input())
linkedLst = LinkedList()
for i in lst:
    linkedLst.append(i)

for i in range(N):
    temp = sys.stdin.readline().strip()
    if len(temp) > 1:
        a, b = temp.split()
        linkedLst.append(b)
    else:
        if temp == 'L':
            linkedLst.left()
        elif temp == 'D':
            linkedLst.right()
        elif temp == 'B':
            linkedLst.delete()
linkedLst.print()
