def caljie(n):
    if n > 1:
        result = caljie(n-1) * n
    else:
        result = 1
    return result

if __name__ == '__main__':
    result1 = caljie(4)
    print(result1)

