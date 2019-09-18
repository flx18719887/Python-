# coding=gbk
#-*- coding:utf-8 -*-
count = 0
age = 21
while count <= 3:
    mage = int(input("输入你猜的年龄："))
    if age == mage:
        print("You have guessed right!")
        break
    elif mage < age:
        print("Guess smaller!")
    else:
        print("Guess bigger!")
    count += 1
    if count == 3:
        print("你是否还想玩？(y or n)")
        option = input("你的选择：")
        if option == "y" and option == "Y":
            count = 0
        else:
            break
print("-------------------------------end--------------------------")