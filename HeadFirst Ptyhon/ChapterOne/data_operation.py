with open('.\data\sunyang.txt') as record_sunyang:
    sunyang=record_sunyang.readline().strip().split(',')
with open('./data/Phelps.txt') as record_phelps:
    phelps=record_phelps.readline().strip().split(',')#方法串链，从左到右读

print(sorted(sunyang))#函数串链，从右到左读

#in placing sort(原地排序)，按指定的顺序排序 ，替换原数据，列表的sort方法，简言：转换后替换(原列表)
#copied sort 复制排序，按指定的顺序排序，返回元数据的副本，原数据保留原来的顺序，BIF sorted支持复制排序，简言：转换后返回(新列表)
print('原数据',sunyang)
sunyang_copied= sorted(sunyang)
print('复制排序后数据',sunyang_copied)
print('原数据',sunyang)
sunyang.sort()
print('原地排序后数据',sunyang)

#format data
def clean_data(time_str):
    if  '-' in time_str:
        split_str='-'
    elif ':' in time_str:
        split_str=':'
    else:
        return(time_str)
    (mins,seconds)=time_str.split(split_str)
    return mins+'.'+seconds
#1.创建新列表存储新数据
clean_sunyang=[]
clean_phelps=[]
#2.迭代老列表中的各项数据
#3.完成格式化数据（转换数据）
#添加到新列表
for each in sunyang:
    clean_sunyang.append(clean_data(each))

for each in phelps:
    clean_phelps.append(clean_data(each))

print('clean data of sun yang:',clean_sunyang)
print('clean data of phelps:',clean_phelps)

print('sorted data of sun yang:',sorted(clean_sunyang))
print('sorted data of phelps:',sorted(clean_phelps))



#1.过程式编程 2.函数式编程  3. 面向对象编程
#列表推导【函数编程概念】
#[列表推导]将简化上述4个步骤,  使用情况：可以快速的对列表项做相同的操作,这个操作是必须要做的，无法排除个别项，若需对个别数据特殊处理，需用迭代方式处理，具有更好的灵活性
clean_sunyang=[clean_data(each)for each in sunyang]
clean_phelps=[clean_data(each) for each in phelps]

print('clean data of sun yang:',clean_sunyang)
print('clean data of phelps:',clean_phelps)

print('sorted data of sun yang:',sorted(clean_sunyang))
print('sorted data of phelps:',sorted(clean_phelps))

print('列表推导例子：')
datas=[1,2,3,4,5]
#生成一个列表，其数据是datas中的平方数
new_datas=[each*each for each in datas]
print('原列表',datas,'\n','平方列表：',new_datas)

print('排序，去重：')
#对排序后的列表进行去重操作,取三次最好成绩
#定义两个列表
unique_sunyang=[]
unique_phelps=[]
sorted_sunyang=sorted(clean_sunyang)
sorted_phelps=sorted(clean_phelps)
#迭代排序后的列表
for each in sorted_sunyang:
    if each not in unique_sunyang:
        unique_sunyang.append(each)
print('sun yang\'s top three records:',unique_sunyang[0:3])

for each in sorted_phelps:
    if each not in unique_phelps:
        unique_phelps.append(each)
print('phelps\'s top three records:',unique_phelps[0:3])

print('排序，去重优化：')
#去重操作优化,用集合（set）删除重复项，数学上的集合
#1.集合中的数据是无序的
#2.天生不重复
#3.使用BIF set创建一个集合
#4.集合使用{}表示

#创建一个空集合
none_set=set()
#创建一个集合，并初始化值
set1={1,2,'ddd','sss'}

#对clean的运动员数据进行去重，然后排序，使用set去重
top_three_records_sunyang= sorted(set(clean_sunyang))[0:3]
top_three_records_phelps= sorted(set(clean_phelps))[0:3]
print('top three records of sunyang:', top_three_records_sunyang)
print('top three records of sunyang:', top_three_records_phelps)

top_three_records_phelps= sorted(set([clean_data(each) for each in sunyang]))[0:3]
print('top three records of sunyang:', top_three_records_sunyang)
print('top three records of sunyang:', top_three_records_phelps)

#改善代码质量
#1.必要的地方添加代码注释
#2.把一些重复的代码提取函数
#3.做好代码异常处理

#优化后的代码
#format data
def clean_data1(time_str):
    #1.注释：这是对数据的特殊处理
    if  '-' in time_str:
        split_str='-'
    elif ':' in time_str:
        split_str=':'
    else:
        return(time_str)
    (mins,seconds)=time_str.split(split_str)
    return mins+'.'+seconds

def read_record_file(filename):
    #2.异常处理
    try:
        with open(filename) as recordfile:
            record = recordfile.readline().strip().split(',')
        return [clean_data1(each) for each in record] #应该将这个代码提到函数外，功能单一
    except IOError as err:
        print(str(err))
    except:
        print('other error!')
#3.重复代码，提取函数
sunyang=read_record_file('./data/sunyang.txt')
phelps=read_record_file('./data/phelps.txt')
print(sunyang,'\n',phelps)

top_three_records_sunyang=sorted(read_record_file('./data/sunyang.txt'))[0:3]
print('top three records of sunyang:', top_three_records_sunyang)

top_three_records_phelps=sorted(read_record_file('./data/sunyang.txt'))[0:3]
print('top three records of sunyang:', top_three_records_phelps)

print('空集合:',set())
set_a=set1={1,2,'ddd','sss','1','2',1,2,'1','2'}
print('去重集合:',{1,2,'ddd','sss','1','2',1,2,'1','2'})
print('list 转换为 set:',set([1,2,2,1]))
# print(set('1',1,1,2,'1','2'))
# #关键内容
# 1.原地排序：转换后替换(原序列)  list.sort()
# 2.复制排序：转换后返回(新序列)  BIF sorted()
# 3.方法串链：从右往左读  ' a,b,c  '.strip().split(',')
# 4.函数串链：从左往右读或从里往外读 print(sorted(sunyang))
# 5.列表推导  pingfang= [each*each for each  in [1,2,3]]
# 6.分片 slice [1,2,3][0:2]
# 7.集合-一组无序无重的数据项，set1={1,2,'ddd','sss','1','2',1,2,'1','2'}|||set()=>{}|||set([1,2,1,2])=>{1,2}