#!/usr/bin/python3

""" Module that defines Node class and SinglyLinkedList  class """


class Node:
    """ Class that models a Node object """
    def __init__(self, data, next_node=None):
        """ constructor for Node instance """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if next_node is None or isinstance(next_node, Node):
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """ a class model for a singly linked list """
    def __init__(self):
        """ head of the linked list """
        self.__head = None

    def __str__(self):
        tmp = self.__head
        if tmp is None:
            return ''
        while tmp is not None and tmp.next_node is not None:
            print(tmp.data)
            tmp = tmp.next_node
        return f"{tmp.data}"

    def sorted_insert(self, value):
        """ insert a node to a sorted linked list

        n (Node): new node
        c (Node): current node
        """
        n = Node(0)
        n.data = value
        n.next_node = None
        if self.__head is None:
            self.__head = n
            return
        c = self.__head
        while c is not None:
            if n.data >= c.data:
                if c.next_node is None or n.data <= c.next_node.data:
                    n.next_node = c.next_node
                    c.next_node = n
                    return
            if n.data < c.data:
                break
            c = c.next_node
        n.next_node = self.__head
        self.__head = n
