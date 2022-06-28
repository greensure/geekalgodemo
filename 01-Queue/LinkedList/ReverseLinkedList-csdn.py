'''
Author: greensure greensure@sina.com
Date: 2022-06-17 10:47:56
LastEditors: greensure greensure@sina.com
LastEditTime: 2022-06-17 14:10:34
FilePath: \GeekAlgoDemo\01-Queue\LinkedList\ReverseLinkedList-csdn.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# https://blog.csdn.net/kongsuhongbaby/article/details/106630731

# 1)创建一个新的空列表；
# 2）取出旧链表中头结点的元素，将其next指针设置为新链表的头指针，同时将旧链表的头结点执行下一个元素

import copy

class Node:
     """节点类，包含值和下一个节点的指针"""
     def __init__(self, value, next = None):
        self.value = value
        self.next = next

     def __str__(self):
        return "Node value:%s" % self.value

class LinkedList:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
    
    def get_all(self):
        """获取链表中所有的节点"""
        nodes = []
        temp = self.head
        while temp:
            nodes.append(temp.value)
            temp = temp.next
        return nodes

    def add_node(self, value):
        """在列表中添加节点"""
        node = Node(value)
        # 空链表,收尾指针都指向新增加的节点
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    def reverse_list(self):
        """
        反转单向列表
        思路一：先对原链表做头删操作，再对新链表做头插
        """
        # 定义一个新的链表
        new_list_node = LinkedList()
        temp = copy.deepcopy(self.head)
        while temp:
            #  1.对之前的链表做头删除操作
            node = temp
            temp = temp.next

            # 2.对新的链表做头插入操作
            if new_list_node.head is None:
                new_list_node.tail = node
            node.next = new_list_node.head
            new_list_node.head = node
        return new_list_node

if __name__ == "__main__":
    l = LinkedList()
    for i in range(5):
        l.add_node(i)
    new_list_node = l.reverse_list()
    print(new_list_node.get_all())
    print(new_list_node.tail)



