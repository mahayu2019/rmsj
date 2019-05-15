#!/usr/bin/env python
# coding=utf-8

bicycles = ['trek', 'canon', 'redline', 'spec']
print(bicycles)
print(bicycles[2])
print(bicycles[1].title())  # 首字母大写
print(bicycles[-1])  # 最后一个元素

# 修改元素
bicycles[1] = '修改的'
print(bicycles)

# 结尾添加元素
bicycles.append('新增元素')
print(bicycles)

# 指定位置添加元素
bicycles.insert(3, 'appeal')
print(bicycles)

# 删除指定位置元素
del bicycles[2]
print(bicycles)

# 从结尾弹出元素
bicycles.pop()
print(bicycles)

# 从指定位置弹出元素
bicycles.pop(0)
print(bicycles)

# 根据值删除元素,重复元素只删除第一个
bicycles.remove('spec')
print(bicycles)
