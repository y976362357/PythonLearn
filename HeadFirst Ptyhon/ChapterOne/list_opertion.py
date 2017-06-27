#Notice:Python的变量标识符没有类型
#列表就像是数组，
#电影列表
movies=['变形金刚1','变形金刚2','变形金刚3','变形金刚4','变形金刚5']

#使用中括号记法访问列表数据
print(movies[0])#输出变形金刚1
print("Len内置函数",len(movies))

#使用append方法添加元素
print(movies)
movies.append('变形金刚6')
print(movies)

#使用 pop删除元素
#    L.pop([index]) -> item -- remove and return item at index (default last).
#        Raises IndexError if list is empty or index is out of range.
movies.pop()
print(movies)

#remove item
# L.remove(value) -> None -- remove first occurrence of value.
# Raises ValueError if the value is not present.
print(movies)
movies.append("test")
print(movies)
movies.remove('test')
print(movies)

#在列表第一个位置插入元素test，使用pop移除第一个插入的 元素
''' L.insert(index, object) -- insert object before index '''
movies.insert(0,'test')
print(movies)
movies.pop(0)
print(movies)

#extend  使用list扩展list
#L.extend(iterable) -> None -- extend list by appending elements from the iterable
#list 可以存储任意类型的数据，列表存储混合类型的诗句
movies.extend([1,2])
movies.extend((3,4))
print(movies)

 # 迭代list
 #Python 中的for 就是为了处理list和其他迭代结构
print('Movie List:')
for each_movie in movies:
     print(each_movie)

#while迭代list
count=0
while count<len(movies):
    print(movies[count])
    count+=1
#while需要提供额外的条件实现迭代

#列表嵌套
school=['一年级',['1(1)班',['A','B','C','D'],'1[2]班',['E','F','G']]]
print(school[1][1][1])

for item in school:
    print(type(item))
    if isinstance(item,list):
        print('list type')
    elif isinstance(item,str):
        print('str type')
    else:
        print("not list type")


def print_list2(the_list,level):
    for item in the_list:
        if isinstance(item,list):
            print_list2(item,level+1)
        else:
            for i in range(level):
                print("\t",end='')
            print(item)

def print_list(the_list):
    for item in the_list:
        if isinstance(item,list):
            print_list(item)
        else:
            print(item)
print_list(school)
print_list2(school,0)
import  sys
sys.path.insert(0,'test')
print(sys.path)