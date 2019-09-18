# mstring1 = "nihao "
# mstring2 = "haha "
# mstring3 = "A"
# # 字符串的拼接  +
# print(mstring1 +  mstring2)
#
# # 字符串的重复 *
# print(mstring2 * 4)
# print(mstring3 * 7)

# 字符串索引 []
# mstr1 = "bigbang"
# print(mstr1[0])
#
# # 字符串切片 [:]
# print(mstr1[:])
# print(mstr1[2:4])  # 包头不包尾 取索引为2,3号元素
# print(mstr1[:4])  # 包头不包尾 取索引为0,1，2,3号元素
# print(mstr1[3:])
# print(mstr1[-1:-4])
#
# print("44" not in "1234")

# 创建字符串hello world，将其中的world更新为bawei
# mstr = "hello world"
# mstr1 = mstr[:6] + "bawei"
# print(mstr1)

# 从控制台输入一个字符串，判断它是否是回文字符串
# 121343121

# mstr = input("please enter your num:")
# if mstr == mstr[-1:]:
#     print("回文字符串")
# else:
#     print("不是回文字符串")
#
# str = "hello world"
# print(str * 3)






# 请输出十个”hello bawei”


# # 1.	分别输入两个字符串，输入两个字符串的拼接字符串（50分）
# mstr1 = input("enter one string: ")
# mstr2 = input("enter another string: ")
# mstr = mstr1 + mstr2
# print(mstr)



# # 2.	输入一个数字，将接收到的值转换为int类型，并打印该变量的类型。
# mnum = input("enter a num: ")
# print(type(mnum))
# mnum = int(mnum)
# print(type(mnum))



# mlist = ["A", "B", "C", "D", "E"]
# mlist.extend(["F", "G", "H", "M"])
# # mlist.insert(9,"Z")
# print(mlist)


# 通过用户输入数字，计算阶乘。（30分）

# mnum = int(input("please enter a number: "))
#
# def jiechen(mnum):
#     return mnum * jiechen(mnum - 1)
#
#
# jiechen(mnum)





# 2. 判断101-200之间有多少个素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。（30分）
#
# 3. 将一个列表的数据复制到另一个列表中，并反向排序输出。






