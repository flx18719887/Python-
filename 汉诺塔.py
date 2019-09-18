a = "A"
b = "B"
c = "C"
def hano(a, b, c, n):
    if n == 1:
        print("{}-->{}".format(a, c))
        return None

    if n == 2:
        print("{}-->{}".format(a, c))
        print("{}-->{}".format(a, b))
        print("{}-->{}".format(b, c))
        return None

    hano(a, c, b, n-1)
    print("{}-->{}".format(a, c))
    hano(b, a, c, n-1)

# 只有一个盘子
print("只有一个盘子")
hano(a, b, c, 1)

# 只有2个盘子
print("只有2个盘子")
hano(a, b, c, 2)

# 只有2个盘子
print("只有5个盘子")
hano(a, b, c, 5)


