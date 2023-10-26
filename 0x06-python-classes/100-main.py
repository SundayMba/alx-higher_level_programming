#!/usr/bin/python3
SinglyLinkedList = __import__('100-singly_linked_list').SinglyLinkedList
Node = __import__('100-singly_linked_list').Node

sll = SinglyLinkedList()
"""sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)"""

n1 = Node(1)
print(n1.data)
n2 = Node(3)
print(n2.data)
n3 = Node(4)
n3.nextnode = n2
print(n3.nextnode.data)
try:
    n4 = Node("7")
except Exception as e:
    print(e)
try:
    n2.next_node = "Node"
except Exception as e:
    print(e)
print(sll)
