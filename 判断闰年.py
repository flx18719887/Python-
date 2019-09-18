if __name__ == '__main__':
# 1.能被400整除的年份
# 2.能被4整除，但是不能被100整除的年份
# 3.以上2种方法满足一种即为闰年
    year = input("请输入年份：")
    if year.isdigit() and len(year) == 4:
        year = int(year)
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            # print("您输入的%s是闰年！" % year)
            print("您输入的{}是闰年！".format(year))
        else:
            # print("您输入的%s是平年！" % year)
            print("您输入的{}是平年！".format(year))
    else:
        print("输入有误，请重新输入：")

