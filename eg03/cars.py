#!/usr/bin/env python
# coding=utf-8

# sort 永久性排序,原始序列被修改
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# 逆序排列
cars.sort(reverse=True)
print(cars)

# sorted排序,不改变原始列表顺序
cars2 = ['bmw', 'audi', 'toyota', 'subaru']
print("原始顺序:")
print(cars2)

print("sorted排序:")
print(sorted(cars2))

print("检测对比:")
print(cars2)

# 反转列表
cars2.reverse()
print(cars2)

# 列表长度
print(len(cars2))
