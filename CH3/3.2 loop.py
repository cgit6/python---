'''
loop 常用於重複的事情
在iterable object (string,list,dict,tuple,set)皆可使用loop

for variable in iterable:
    do thing
'''
# for loop (str,list,tuple,dict)
str = "abc"
for i in str:
    pass

# list
list = [1,3,5,7,9]
for i in list:
    print(i)

# tuple
tuple = [(1,3),(3,5),(5,7),(7,9)]
for i in tuple:
    print(i)

for i,j in tuple:
    print(i,j)

# dictionary 
dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
for key in dict.keys():
    pass
for value in dict.values():
    pass
for item in dict.items():
    pass

# set
set = {1,2,3,4,5,6,7,8,9}
for i in set:
    pass

'''
while loop
當不確定要執行幾次時使用 while

while (if condition=true):
    do thing

有可能存在無限迴圈的問題
'''
# while loop str
t = 0
while t < 5:
    print(t)
    t += 1 # 一定要有這個

'''
outer loop: 外面那層
inner loop: 裡面那層
'''
# nested for loop
for i in "1234":
    for j in "abcd":
        pass


# pass , break , continue
'''

用於if,loop,function,class
pass: 跳過

用於 for loop
break: 中止當前迭代過程
continue: 跳過第t次迭代
'''

# break
for i in "123456789":
    if i =="5":
        break
    else:
        print(i)

# break in nested loop
for i in "1234":
    # if ... break
    for j in "abcdefghi":
        if  j =="e":
            break
        else:
            print(i,j)



# continue
for i in "123456789":
    if i =="5":
        continue
        #在continue下方的code都不會被執行
    else:
        print(i)
 