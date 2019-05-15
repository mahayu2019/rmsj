#!/usr/bin/env python
# coding=utf-8

# 练习3-1
names = ['张三', '李四', '王五', '赵六', '孙武']
for i in names:
    {
        print(i)
    }

# 练习3-2
for wh in names:
    {
        print('你好,' + wh + '欢迎光临!')
    }

# 练习3-3
jt = ['自行车', '汽车', '火车', '飞机']
for k in jt:
    {
        print('坐' + k + '去打架')
    }

# 练习3-4
mans = []
mans.append('娃哈哈')
mans.append('喜羊羊')
mans.append('猴子')
mans.append('老猪')
mans.append('雷子')
for f in mans:
    {
        print(f + '来玩哈')
    }

# 练习3-5
print(mans[0] + ',' + mans[3] + '无法赴约')
mans[0]='哈利波特'
mans[3]='达芬奇'
for f in mans:
    {
        print(f + '来玩哈')
    }

# 练习3-6