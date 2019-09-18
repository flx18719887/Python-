if __name__ == '__main__':

    # 已知字符串a=’aAsmr3idd4bgs7Dlsf9eAF’要求如下:
    # 1.	将字符串中的数字取出组成一个新的字符串并输出，8分
    # a="aAsmr3idd4bgs7Dlsf9eAF"
    # mlist = []
    # for i in range(len(a)):
    #     if a[i].isdigit():
    #         mlist.append(a[i])
    # mstr = "".join(mlist)
    # print(mstr)

    # # 方法2
    a="aAsmr3idd4bgs7Dlsf9eAF"
    print("".join([s for s in a if s.isdigit()]))

    # 2.	请统计a字符串出现的每个字母的出现次数（区分大小写，a与A不是同一个字母），8分
    print(dict([(x, a.count(x)) for x in set(a)]))

    # 3.	输出a字符串出现频率最高的字母，8分
    mlist = ([(x, a.count(x)) for x in set(a)])
    mlist.sort(key=lambda k: k[1], reverse=True)
    print(mlist[0][0])


    # 4.	请将a字符串反转并输出。例：’abc’的反转是’cba’，8分
    a = "aAsmr3idd4bgs7Dlsf9eAF"
    print(a[::-1])

    # 5.	请判断 ‘boy’里出现的每一个字母，是否都出现在a字符串里。如果是，则输出True，否则，则输出False，8分
    mset = set(list(a))
    print(mset)
    boy_set = set(list('boy'))
    print(boy_set)
    # 计算当前a集合的长度
    x = len(mset)
    # 将boy集合放入a集合
    mset.update(boy_set)
    print(mset)
    # 再次计算更新后的a结合的长度
    y = len(mset)
    # 判断两次计算的长度是否相等，相等输出True，不相等输出False
    if x == y:
        print("True")
    else:
        print("False")
