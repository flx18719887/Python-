if __name__ == '__main__':
    # for i in range(1, 10):
    #     for j in range(1, 10):
    #         if j <= i:
    #             print(i, "*", j, "=", i*j, end = "    ")
    #     print("\n")

# //////////////////////////////////////////////////////////////////////////////
#     for i in range(1, 10):
#         for j in range(1, 10):
#             if j <= i:
#                 print('{}*{}={}'.format(i, j, i * j), end='\t')
#                 j+=1
#         print('\n')
#         i+=1



# //////////////////////////////////////////////////////////////////////////////
    # for i in range(1, 10):
    #     for j in range(1, 10):
    #          if j <= i:
    #             print('%s * %s = %s' % (i, j, i * j), end='\t')
    #     print()

# //////////////////////////////////////////////////////////////////////////////
#     for i in range(1, 10):
#         for j in range(1, i+1):
#             print(str(i) + '*' + str(j) + '=' + str(i*j), end='\t')
#         print()

    for i in range(9, 0, -1):
        for j in range(9, 0, -1):
            if j <= i:
                print('%s * %s = %s' % (i, j, i * j), end='\t')
        print()



# //////////////////////////////////////////////////////////////////////////////
    # i = 1
    # while i <= 9:
    #     j = 1
    #     while j <= i:
    #         print(i, "*", j, "=", i*j, end = "    ")
    #         j += 1
    #     print("\n")
    #     i += 1



    # i = 1
    # while i <= 9:
    #     j = 1
    #     while j <= i:
    #         print('{}*{}={}'.format(i, j, i * j), end='\t')
    #         j += 1
    #     print('\n')
    #     i += 1
