#!/usr/bin/env python
# -*- coding: utf-8 -*-


def list_max(nums:list, max_num=float("-inf")):
    # 基线条件为nums为空
    if not nums:
        return max_num
    # 隐含的递归条件为nums不为空
    num = nums.pop()
    if num > max_num:
        max_num = num
    # 尾递归
    return list_max(nums, max_num)


nums = [10, 1000000, 3, 9999]

result = list_max(nums)
print(result)