#第三章，文件与异常
#Python的open()BIF 就是用来与文件交互。
#读取movies列表
import os


path='../../Day1/data/'#..表示当前目录的父目录   .表示当前目录
filename='movies.txt'

if  os.path.exists(path+filename):#文件夹存在
    pass
else:
    print('file not found', path + filename)
    filename='movies.txt'
the_movies_file=open(path+filename,encoding='utf-8')
#print(the_movies_file.encoding)#当前文件打开的encoding方式
print('the first line in the movies file：',the_movies_file.readline(),end='')#读取一行数据
the_movies_file.seek(0)#读文件指针回到起始位置
#循环遍历文件中的每行数据
for each_line in the_movies_file:
    #print(each_line,end='\t')
    #if  each_line.count(',')>0:#统计substr出现的次数
    #if each_line.find(',')>-1:  # 查找某字符串出现的index，未找到则返回-1
    if not each_line.find(',')==-1:
        (name,time)=each_line.split(',',1)
        print('name:',name,'time:',time,end='')
    else:
        print(each_line,end='')
#关闭文件
the_movies_file.close()


try:
    the_movies_file=open(path+filename,encoding='utf-8')
    print('the first line in the movies file',the_movies_file.readline(),'')
    the_movies_file.seek(0)
    for each_line in the_movies_file:
        try:
            (name,time)=each_line.split(',',1)
            print('Name:',name,'\t','Time:',time,end='')
        except ValueError:
             print('ValueError')
        except:
            print('other error!')
    the_movies_file.close()
except IOError:
    print(path+filename,' not found!',end='')
except:
    print('other error!')


print('\r\n','-----------------------------')
""" Return a unicode string representing the current working directory. """
print(os.getcwd())#当前工作目录
print(os.listdir('.'))
print('-------------------------------------------')
#列出某个目录下的所有文件及文件夹名称列表
path='../../Day1/data/'
for item in os.listdir(path):
    file=path+item
    if os.path.isdir(file):
        print(file,' is directory!',end='')
    elif os.path.isfile(file):
        print(file,' is file！',end='')
    else:
        print(file,' is other type!')

try:
    a,b=2,0
    c=a/b
except IOError:
    print('error',end='')
except ZeroDivisionError:
    print('ZeroDivisionError')

print(os.listdir(os.getcwd()))
os.chdir('data')#切换到data目录
print(os.getcwd())#当前工作目录
