#!/usr/bin/env python
# coding=utf-8

# ex4-3
for i in range(1, 21):
    print(i)

# ex4-4
bws = []
for i in range(1, 100):
    bws.append(i)

for j in bws:
    print(j)

# ex4-5
nums = []
for n in range(1, 1000001):
    nums.append(n)

print(min(nums))
print(max(nums))
print(sum(nums))

# ex4-6
js = []
for k in range(1, 21, 2):
    js.append(k)
for x in js:
    print(x)

# ex4-7
san = []
for num in range(3, 30, 3):
    san.append(num)
for xnum in san:
    print(xnum)

# ex4-8
lf = []
for num in range(1, 10):
    lf.append(num ** 3)

print(lf)
