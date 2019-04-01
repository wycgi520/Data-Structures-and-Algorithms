#!/usr/bin/env python
#coding=utf-8


nums = [1, 2, 3, 4, 5]
# 基线条件为nums为空, 递归条件为nums不为空
list_sum = lambda nums : nums.pop() + list_sum(nums) if nums else 0
result = list_sum(nums)
print(result)