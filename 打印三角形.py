if __name__ == '__main__':
    # num = int(input("请输入个数："))
    # i = 1
    # while i <= num:
    #     j = 1
    #     while j <= i:
    #         print("*", end = " ")
    #         j += 1
    #     print("\n")
    #     i += 1



    num = int(input("enter a num: "))
    for i in range(1, num):
        for j in range(1, num):
            if j <= i:
                print("*", end = " ")
        print("\n")