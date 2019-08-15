#关于字典的应用
databook = {"siri":'123456',"zhu":'123456',"admin":'123456'}
databook_2 = databook.copy()
print(databook_2)
databook_3=dict()
databook.clear()
databook_3["name"]=("siri",'siri123456','true','male') #使用元组放置放置信息,键-值 值使用元组表示
print(databook_3)
print(databook_3["name"][1].title()) #读取元组内的数据,使用列表的语法读取
print("name = {name}".format_map(databook_3))#完整读取name中的信息
print("name = {name[1]}".format_map(databook_3))#读取name中值的部分信息
print (databook_3.items())
print(databook_3.keys())
databook_3.update(databook_2)
print (databook_3)
databook_3.update(databook_2)
print (databook_3)


print (databook_3.items())
print(databook_3.keys())
databook_3.update(databook_2)
print (databook_3)
databook_3.update(databook_2)
print (databook_3)

