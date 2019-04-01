#!/usr/bin/env python
# -*- coding:utf-8 -*-

def Selection_sort(li, reverse=False):
    """默认升序序列"""
    li_sort = list()
    while True:
        if len(li) == 0: break
        # 循环数列, 默认找到最小值,并取出最小值并添加到新序列中
        num_taken = li[0]
        for num in li:
            if reverse:
                num_taken = max(num_taken, num)
            else:
                num_taken = min(num_taken, num)
        li.remove(num_taken)
        li_sort.append(num_taken)

    return li_sort

nums_need_sorted = [5, 2, 8, 3]

New_list = Selection_sort(nums_need_sorted, reverse=True)

print(New_list)