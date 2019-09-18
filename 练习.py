# mstr = "I am %s, and I have %d book"
# print("mstr---", mstr %("flx", 3))
# mstr1 = "I am %s, and I have %d book" %("flx", 5)
# print("mstr1---",mstr1)
# mstr2 = "I am {0}, and I have {1} pen, and I love {2}".format("jack", 10, "北京")
# print("mstr2---", mstr2)
# mstr3 = "I am {0}, and I have {2} pen and {1} book".format("jack", 10, 19)
# print("mstr3---", mstr3)

# print("{name} 的年龄是 {age}".format(name="小明", age = "12"))
# print("{0} 的年龄是 {1}".format("花花", 13))
# print("{} 的年龄是 {}".format("乐乐", 15))
# print("%s 的年龄是 %d" %("芳芳", 16))


# score = int(input("enter your score: "))
# if score>60 and score<70:
#     print("及格")
# elif score > 70 and score < 80:
#     print("一般")
# elif score>90:
#     print("优秀")
# else:
#     print("不及格")


# import random
# random.randint(a, b): 返回a到b范围内任意一个整数值
# # randint  随机从给定的范围取一个整数
# val = random.randint(1, 5)
# print(val, "\n---------------------------")
#
# for i in range(10):
#     print(i, end = "")
#
# # choice  从已经给定的序列中随机选择一个数值
# print("\n---------------------------")
# var = random.choice(range(10))
# print(var)
#
# var1 = random.choice(range(5))
# print("var1 = {var1}".format(var1 = var1))

# import random
# mstr = "abcdkjlafjlsdaldghehidv"
# newmstr = ""
# for i in range(5):
#     newmstr += random.choice(mstr)
#     print(i, newmstr)

# import random
# # 在1到10范围内生成随机数值
# var = random.randrange(1, 10)
# print("var = {var}".format(var = var))


# import random
# mlist = [1, 2, 3, 9, 4, 3]
# # 每次对指定的列表执行随机打乱顺序
# random.shuffle(mlist)
# print(mlist)
# mlist.sort()
# print(mlist)


# import random
# mlist1 = [i for i in range(1, 10,1)]
# print(mlist1)
# mlist2 = [i for i in range(10, 1, -1)]
# print(mlist2)



# 创建列表
# mlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(mlist)
# mlist1 = [i for i in mlist if i%2 == 1]
# print(mlist1)
# print("-----------------------------------------------------------------------")
# alist = [1, 2, 3, 4, 5, 6, 7]
# blist = [3, 4, 5, 6, 7, 8, 9]
# clist = [a + b for a in alist for b in blist]
# print(clist)
# dlist = [a + b for a in alist if a%2 == 0 for b in blist  if b%2 == 1]
# print(dlist)
# print("-----------------------------------------------------------------------")
# rlist = [['u', 'v'], ['p', 'q'], ['i', 'j']]
# slist = [[m, n] for m, n in rlist]
# print(slist)



# 复制列表
# 索引([:])——（复制整个列表）创建一个始于第一个元素，终止与最后一个元素的切片。
# 赋值
alist = [5, 4, 3, 2, 1]
blist = alist
blist[4] = 0
print("alist:", alist)
print("blist:", blist)
# 复制
clist = [9, 8, 7, 6, 5]
dlist = clist[:]
dlist[4] = 0
print("clist:", clist)
print("dlist:", dlist)
print("clist = {}".format(clist))
print("dlist = {}".format(dlist))


















