#!/usr/bin/env python
#coding=utf-8

def binary_search(stuff, list_sort):
    low = 0
    high = len(list_sort)-1

    while low <= high:
        mid = (low+high)//2
        ele = list_sort[mid]
        if stuff == ele:
            return mid
        elif stuff > ele:
            # 原来没写加1, 使得在找不到数字时跳不出循环
            low = mid + 1
        else:
            # 同上, 应该写上减1, 以便能够顺利跳出循环
            high = mid - 1

    return None

list_nums = [1, 2, 3, 4]

stuff_location = binary_search(10, list_nums)

print(stuff_location)