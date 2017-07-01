

#格式化距离字符串，将’-‘，’：‘，替换伟'.'并返回
def format_time(time_str):
    if '-' in time_str:
        split_str='-'
    elif ':' in time_str:
        split_str=':'
    else:
        return  time_str;
    (m, s)=time_str.split(split_str)
    return m+'.' + s;

#读取记录文件,并返回一个list
def read_record_file(filename,type='list'):
    pass
    try:
        with open(filename) as file:
            data=file.readline().strip().split(',')
            if type=='list':
                return data
            else:
                return {'Name':data.pop(0),
                         'Date':data.pop(0),
                        "AllRecords":[format_time(each) for each in data],
                        "Top_Three_Records": sorted(set(format_time(each) for each in data))[0:3]
                        }
    except IOError as err:
        print('File error: ',str(err))
        return (None)
    except :
        print('Other error!')
        return(None)


print('Toby每天都骑自行车，这是2017-6-31，每次骑行花的时间:')
toby_records=read_record_file('./data/Toby.txt')
#移除列表的元素并返回
(name,date)= toby_records.pop(0), toby_records.pop(0)
print(name +'\'s top three records on ' + date + ' are ', sorted(set(format_time(each) for each in toby_records))[0:3])

print('下面我们将说说字典的这数据类型：')
#如何创建一个字典
toby={}
kun=dict()#工厂函数
toby['Name']='Toby'
kun["Name"]='Kun'
print(toby["Name"])#KeyError ,当key不存在时会出现。。
print(toby,kun,type(toby),type(kun))

print('下面我们将用字典的方式处理上述的问题：')

print('Toby每天都骑自行车，这是2017-6-31，每次骑行花的时间:')
toby_records=read_record_file('./data/Toby.txt')
#移除列表的元素并返回
toby["Name"]=toby_records.pop(0)
toby["Date"]=toby_records.pop(0)
toby["AllRecords"]=[format_time(each) for each in toby_records]
toby["Top_Three_Records"]=sorted(set(format_time(each) for each in toby_records))[0:3]

print(toby["Name"] +'\'s top three records on ' + toby["Date"] + ' are ', toby["Top_Three_Records"])
print(toby["Name"] +'\'s all records on ' + toby["Date"] + ' are ', toby["AllRecords"])

print('现在扩展了read_record_file方法，使其可以返回一个dict：')
dict_toby=read_record_file('./data/Toby.txt','dict')
print(dict_toby["Name"] + '\'s top three records on ' + dict_toby["Date"] + ' are ', dict_toby["Top_Three_Records"])
print(dict_toby["Name"] + '\'s all records on ' + dict_toby["Date"] + ' are ', dict_toby["AllRecords"])


#字典是一个内置的数据结构，允许将数据值与键关联,键-字典中查找的部分，字典中的数据部分（可以是任何值，也包括另一种数据结构)
#self这是一个方法参数，总是指向当前对象实例