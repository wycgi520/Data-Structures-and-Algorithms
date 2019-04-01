#!/usr/bin/env python
# -*- coding: utf-8 -*-


def binary_search(nums: list, i, j, num):
    # 基线条件, 找到最后一个, 索引i和j相等
    if j == i and nums[i] != num:
        return None
    mid = (j+i)//2
    # 递归条件, 中间数与查找值的大小关系
    if nums[mid] == num:
        return mid
    elif nums[mid] > num:
        return binary_search(nums, i, mid-1, num)
    else:
        return binary_search(nums, mid+1, j, num)


nums = [1, 2, 3, 4, 5, 6, 7]

result = binary_search(sorted(nums), 0, len(nums), 6)

print(result)
