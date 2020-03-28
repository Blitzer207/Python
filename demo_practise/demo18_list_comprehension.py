'''
List comprehension 列表解析式

list 生成新的list就是一个 list comprehension的过程，

需求： 从 0 - 12 的数字分别乘以 2， 然后放到新的列表里面（list）
'''

newList = []

# for i in range(11):
#     newList.append(i*2)
# print(newList)
# print([i*2 for i in range(11)])

list = ["xiaoming", "wangba", "wanger", "zhaosi"]
# filterlist = []
# for name in list:
#     if name.startswith("wang"):
#         print(name)
#         filterlist.append(name)
# print(filterlist)

print([name for name in list if name.startswith("wang")])