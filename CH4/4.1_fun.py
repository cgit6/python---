

# 為自定義function寫一些介紹內容
def fun3(x):
    # 這叫做 doctring
    '''This function introduced'''
    pass


# 使用help function
help(fun3)

# input => parameter 參數
def fun_name(input):
    pass


# 執行 function execution,invokation
# 在這裡給訂的input 值為arguments 執行function 給訂的值
fun_name(input)

# global variable
a = 5


def fun1(x, y):
    # local variable
    x = 1
    y = 2
    print(x, y, a)

# fun1()


# 存在copy by value or reference 的問題
a = 10

def fun2(x):
    # 需要靠這個把全域變數引入
    global a
    a = 24


fun2(a)
print(a)

# return keyword
def fun3():
    for i in range(10):
        for j in range(10):
            if i ==3 and j ==4 :
                return
            print(i, j)

fun3()

# import functions
# 例如:
from sys import argv
# syntax
# from module import functions

# positional and keyword arguments

# position arguments : 要特別注意順序
def fun4(a,b):
    return a ** b

print(fun4(2,3))
print(fun4(3,2))

# keyword arguments : 順序沒差，但是變數名稱有差
print(fun4(a= 2,b= 3))
print(fun4(b= 2,a= 3))
# 例如
list = [1,2,3]
print(sorted(list,reverse=True))
# list is position arguments
# reverse is keyword arguments
# 兩者可以混合使用

# Default arguments in Python 

# default arguments
def sum(a,b):
    return a + b
print(sum(1,2))
# 假設今天少一個參數呢?

# 例如:
# def sum(a,b):
#     return a+b
# print(sum(1)) // error

# 如何解決?
# Ans: 利用 default arguments 來解決
def sum(b, a=10):
    return a + b

print(sum(1))

# what diff default argument and keyword argument
def sum(n1 = 0,n2 = 0):
    return n1 + n2

print(sum(n2=100,n1=50))