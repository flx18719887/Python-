# Myfile = open(r"C:\Users\Administrator\Desktop\hel.txt", 'w')
# Myfile.write("I am very happy, and you?")

Myfile1 = open(r"C:\Users\Administrator\Desktop\Myfile\hello3.txt", 'r')
# strChar = Myfile1.read()    # 按字符读取文件全部内容
# strline = Myfile1.readline()  # 按行读取文件内容
strlines = Myfile1.readlines()   # 读取所有行，并返回列表
print(strlines)
Myfile1.close()
