def fibs(n):
    if n <= 1:
        return n
    return fibs(n-1) + fibs(n - 2)

if __name__ == '__main__':
    for i in range(20):
        print(fibs(i), end = " ")