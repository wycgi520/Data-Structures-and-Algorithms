#!/usr/bin/env python
#coding=utf-8

def list_count(nums:list, count=0):
    # 基线条件, 数组为空
    if nums == []: return count
    # 隐含的递归条件为, 数组不为空
    nums.pop()
    count += 1
    # 尾递归, 虽然python3不支持
    return list_count(nums, count)

nums = [1]
result = list_count(nums)
print(result)