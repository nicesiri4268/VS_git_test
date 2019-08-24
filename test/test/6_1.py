import head_6_1 as h_6
Myname ={}
h_6.init(Myname)
h_6.store(Myname,"mange lie hetland")
print (h_6.lookup (Myname,"middle","lie"))
h_6.store_1(Myname,"luke skywalker","anakin skywalker")
#使用 * 来使函数一次输入多个参数
print (h_6.lookup(Myname, "last","skywalker"))



#递归实践
def factorial(n):
    "递归的基础实现方法"
    result = n
    for i in range(1,n):
        result *=i
    return result
def factorial_1(n):
    if n==1:
        return 1
    else :
        return n*factorial_1(n-1)

print (factorial_1(10),"and",factorial(10))
