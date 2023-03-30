"""
comprehension: 一種程式縮寫的方法 ，更pythonic
syntax: 
new_list = [operation for variable in original_list if condition]
new_dict = {key:value(operation) for variable in original_dict if condition}

"""
# List,Dict,Set,Generator of Comprehension

# 從:
list = [1,2,3,4,5,6]
squared_x = []
for item in list:
    squared_x.append(item**2)

print(squared_x)
# 變成:
new_list = [item**2 for item in list ]
print(new_list)
# 加入condition
new_list = [item**2 for item in list if item > 2 ]
print(new_list)

# dict comprehension
dict = {'a':1, 'b':2, 'c':3, 'd':4}
# dict => new_dict
new_dict = { item : item **2 for item in dict.values()}
print(new_dict)
# list => new_dict
new_dict2 = {item:item**2 for item in list}
print(new_dict2)

# set comprehension
# list => set
new_set = {item**2 for item in list}
print(new_set)
# set => set
set = {1,2,3,4,5,6}
new_set2 = {item**2 for item in set }
print(new_set2)

# generator comprehension
