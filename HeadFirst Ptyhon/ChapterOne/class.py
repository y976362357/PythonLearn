
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

#读取记录文件,并返回一个Biker
def read_record_file(filename,type='list'):
    pass
    try:
        with open(filename) as file:
            data=file.readline().strip().split(',')
            if type=='list':
                return data
            elif type=='dict':
                return {'Name': data.pop(0),
                        'Date': data.pop(0),
                        "AllRecords": [format_time(each) for each in data],
                        "Top_Three_Records": sorted(set(format_time(each) for each in data))[0:3]
                        }
            else:
                return (Biker(data.pop(0),data.pop(0),[format_time(each) for each in data],))
    except IOError as err:
        print('File error: ',str(err))
        return (None)
    except :
        print('Other error!')
        return(None)

class Biker:
    def __init__(self,name,date=None,records=[]):
        self.name=name
        self.date=date
        self.records=records
    def top(self, top):
        return sorted(set(format_time(each) for each in self.records))[0:top]
    def add_record(self,record):
        self.records.append(record)
    def add_records(self,records):
        self.records.extend(records)

class Biker2(list):
    def __init__(self,name,date=None,records=[]):
        list.__init__([])
        self.extend(records)
        self.name=name
        self.date=date
    def top(self, top):
        return sorted(set(format_time(each) for each in self.self))[0:top]

ss=Biker2("ss")


toby=read_record_file('./data/Toby.txt','class')
print(toby,type(toby))
if  toby:
    print(toby.name +"'s top three records on " + toby.date +' are  ', toby.top(3))
    print(toby.name +"'s top four records on " + toby.date +' are  ', toby.top(4))

class NamedList(list):
    def __init__(self,name):
        list.__init__([])
        self.name=name
a=NamedList('aaa')

print(a.name,a,type(a))





