"""
    元组初始化
    元组的大小和内容都不能修改
"""

tup = (4, 5, 6), (7, 8)
# print(tup)

# 可以将任意序列或迭代器转换成元组
list1 = [4, 5, 6]
# print(list1)
# print(tuple(list1))

tupStr = tuple('string')
# print(tupStr)
# print(tupStr[0])

# 元组拼接
# print((4, None, 'foo') + (6, 0) + ('bar',))

# 拆分元组
tup2 = (1, 2, 3)
a, b, c = tup2
# print(a, b, c)

# 变量拆分常用来迭代迭代元祖或列表
seq = [(1, 2, 3), (2, 3, 4), (5, 6, 7)]
# for a, b, c in seq:
#     print('a={0},b={1},c={2}'.format(a, b, c))

# 统计某个词出现的频率
a = (1, 2, 2, 3, 4, 4, 5, 5, 5)
# print(a.count(5))

# 摘取几个元素，其余舍弃
values = 1, 2, 3, 4, 5
x, y, *_ = values
# print(x, y)

"""
    列表
    长度可变，内容可以被修改
"""
# 元组转列表
tup2 = ("foo", "bar")
a_list = list(tup2)
# print(a_list)

# list函数常用来在数据处理中实体化迭代器或生成器
gen = range(10)
# print(gen)
# print(list(gen))

# 添加和删除元素
# append在列表末尾添加元素
a_list.append('wwo')
# print(a_list)

# insert在特定位置插入
a_list.insert(1, 'red')
# print(a_list)

# pop移除并返回指定位置的元素
inx = a_list.pop(2)
# print(inx)

# 可以用remove去除某个值，remove会寻找第一个值并除去
a_list.append("foo")
# print(a_list)
a_list.remove("foo")
# print(a_list)

# 用in, not in可以判断列表是否包含某个值
# 在列表中检查是否存在某个值远比字典和集合速度慢
# print("foo" in a_list)
# print("aaa" not in a_list)

# 串联
b_list = ["floor", "bert"]
# print(a_list + b_list)

# extend方法可以追加多个元素
b_list.extend([7, 8, (2, 3)])
# print(b_list)

# 排序
s = [7, 2, 5, 1, 3]
s.sort()
# print(s)

s2 = ["saw", "small", "he", "foxes"]
s2.sort(key=len)
# print(s2)

"""
    切片可以选取大多数序列类型的一部分
    左闭右开原则
"""
seq2 = [7, 2, 1, 4, 6, 8, 9]
# print(seq2)
# print(seq2[1:5])

# 切片也可以被序列赋值
seq2[3:5] = [6, 7]
# print(seq2)

"""
    序列函数
    可以返回(i,value)元组序列
"""
some_list = ["f", "a", "v", "r"]
# for i, value in enumerate(some_list):
# print(i, value)

# 当你索引数据时，使用enumerate的一个好方法是计算序列（唯一的）dict映射到位置的值：
mapping = {}
# for i, v in enumerate(some_list):
#     mapping[v] = i
# print(mapping)

"""
    zip可以将多个列表、元组或其他序列成对组合成一个元组列表
"""
seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']
zipped = zip(seq1, seq2)
# print(list(zipped))

# zip的常见用法之一是同时迭代多个序列，可能结合enumerate使用
# for i, (a, b) in enumerate(zip(seq1, seq2)):
#     print('{0}:{1},{2}'.format(i, a, b))

# zip也可以用来解压序列
pitches = [("Nolan", "Ryan"), ("Roger", "Clemens")]
first, last = zip(*pitches)
# print(first)
# print(last)

"""
    字典
"""
d1 = {'a': 'some', 'b': '[1,2,3]'}
# print(d1)
# 插入
d1[3] = (1, 2, 3)
# print(d1)

# 判断键是否存在
# print(3 in d1)

# 可以用del关键字或pop方法（返回值的同时删除键）删除值：
del d1[3]
# print(d1)

ret = d1.pop('b')
# print(ret)
# print(d1)

# keys和values是字典的键和值的迭代器方法
# 输出所有的key和value
d2 = {1: 'age', 2: '[4,5,6]'}
# print(list(d2.keys()))
# print(list(d2.values()))

# update方法可以将两个字典融合
d1.update(d2)
# print(d1)

# 用序列创建字典
# 方法1
mapping1 = {}
key_list = [1, 2, 3, 4, 5]
value_list = ['a', 'b', 'c', 'd', 'e']
for key, value in zip(key_list, value_list):
    mapping1[key] = value
print(mapping1)

# 方法2
mapping1 = dict(zip(range(5), reversed(range(5))))
print(mapping1)


