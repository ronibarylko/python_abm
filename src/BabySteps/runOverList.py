# coding=utf-8
import sys

def reverseList(list_val):
    newList = list()
    for value in list_val:
        newList.insert(0, value)
    print(newList)

reverseList([3, 2, 1])
