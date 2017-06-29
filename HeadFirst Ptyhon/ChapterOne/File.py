# 以写模式打开文件
# 使用内置函数open打开文件是使用r 读的方式打开
import os
import sys

filename = './data/test.txt'

# 以w模式打开时，如果文件不存在，就创建文件，如果文件存在，则清空内容并增加内容
# file=open(filename,mode='w')
# #使用print内置函数可以把数据写入到文件中
# print('print built function test',file=file)
# file.close()#一定要记住关闭文件

# 以追加模式打开文件,注意
# file=open(filename,mode='a')
# print(sys.version_info)
# file.write(str(sys.version_info)+'\n')
# file.write('new line data11')
# file.close()

# 使用w+模式打开文件，可以实现写+读,会先清空文件，如果文件不存在，就创建文件
# finally 模块，无论异常是否出现都会执行

# try:
#     file=open(filename,mode='w+')
#     for i in range(20):
#         file.write(str(i)+'\n')
#     #把文件指针移回初始位置，读取一行数据
#     file.seek(0)
#     print(file.readline(),'')
# except:
#     print('some error occurs!')
# finally:
#     file.close()
#     print('close file always  do!')

# Python中的字符串是不可变的，
# str.strip, 移除字符串前后的空格，并返回一个新字符串,相应的有lstrip,rstrip函数
# Python 变量只包含数据对象的引用，数据对象才是真正包含数据
# Python中不可变的数据类型：数值类型、字符串类型、元组类型

# str1=' hi 你好 333 '
# str2='hi,sss,hi'
# print(len(str1))
# '''        If chars is given and not None, remove characters in chars instead.
# '''
# str2=str2.strip('hi')
# print(str2)
# str1=str1.strip()
# print(str1,' len ',len(str1))


#文件操作，提取异常，处理异常，

# try:
#     file = open(filename.replace('test', 'test1'))  # 执行到这一行，抛出IOError,File对象未创建
#     print(file.readline())
# except IOError as err:
#     print('file error', '---', err.strerror)
#     print('file error', '|||', str(err))
# except:
#     print('other error')
# finally:
#     pass
#     # NameError: name 'file' is not defined
#     # locals()-BIF,返回当前作用域所有变量的集合
#     if 'file' in locals():
#         file.close()
#     else:
#         print('变量未创建')

#简化以上代码，with语句会自动帮你关闭打开的文件，with用了上下文管理协议的技术

try:
    with open(filename) as file2,open(filename.replace('test','test1')) as file:
        print(file2.readline())
        print(file.readline())
except IOError as err:
    print('IOError: ',str(err))

#腌制数据，pickle，其实就是序列化与反序列化
import  pickle

pickle_data='data.data'
data=[1,2,3,'123','666','asda',['a','b','c','d']]
#data='eee'
with open(pickle_data,'wb') as file:
    pickle.dump(data,file)#以二进制打开，保存腌制数据
with open(pickle_data,'rb') as file:
    list= pickle.load(file)
    print(list)
    print(type(list))