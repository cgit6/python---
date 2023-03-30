'''
Enumerate function: 枚舉函數把所有的元素遍歷出來 
'''

counters = 0
for i in "1234567890":
    if counters< 3:
        print(i)
    counters += 1

# enumerate fun 會return 一個 tuple(index, value)
for count,iter in enumerate("1234567890"):
    if count<5:
        print(iter)

# zip fun  把多個list 合併成一個tuple

list1 = [1,2,3,4,5,6,7,8]
list2 = ["a","b","c","d","e","f","g"]

for i in zip(list1, list2):
    # 合成最少數量
    print(i)