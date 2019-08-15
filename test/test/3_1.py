import cmath
database = "hello,world {name} {pi:.3f} {big_number:,}!!!"
database2 ="Hello World yes,sir"
print (database.format(name="zhu",pi=cmath.pi,big_number=10**100)) # 字符串的基本用法 format() 替换 P 43
print (database.format(name = "siri",pi=42,big_number= 0000))
print (database.format(name="test_name",pi = 42,big_number= 0000).center(39))
in_put=input('finding : ')
print(database2.find(in_put))

print(database2.title()) #词首大写