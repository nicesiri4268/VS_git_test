i=int(input("i = "))
assert i<=10 ,'i is too bigger ' #测试i是否太大
for number  in range(0,i):
    print (number)

strings=["siri","bulexxxfly","redxxxcat","lady","siri","female"]
for string in strings :
    if 'siri' in string:
        index = strings.index(string)
        strings[index]="zhu"
print (strings)

strings=["siri","bulexxxfly","redxxxcat","lady","siri","female"]

for index,string in enumerate(strings): 
    #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列
    #同时列出数据和数据下标，一般用在 for 循环当中。
    if "siri" in string:
        strings[index]= "zhu"
print (strings)
list_1 =sorted ("hello,world!")
list_2 = reversed ("hello,world!") #返回的不是一个列表,
print(list_1)
print (list_2)
print (list(list_2)) #需要使用list () 函数来进行列表化

girls =["alice","bernice","clarice","apple","biiy"]
boys =["chris","arnold",'bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0],[]).append(girl) ###为字典赋值为列表,返回值为列表###
print (letterGirls)
print ([b+"+"+g for b in boys for g in letterGirls[b[0]]])

dirt = {}
dirt.setdefault("dirt_2",{})
print (dirt)
dirt.setdefault("dirt_2",{}).setdefault("dirt_3",[]).append("siri")
print (dirt)
for i in range(10):
    dirt.setdefault("dirt_2",{}).setdefault("dirt_3",[]).append(i)
print (dirt)
print (dirt.setdefault("dirt_2"))  #返回字典的值

exec(input("输入代码: ")) #直接从用户输入端输入代码,这样做极其危险,所以需要把代码放入到作用域之中
scope ={}
exec(input("请输入代码(安全方式): "),scope)
print (scope.keys())