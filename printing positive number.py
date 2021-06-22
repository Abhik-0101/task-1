list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]
pos_nos = [num for num in list1 if num >= 0]
print("input: ",*list1)
print("output: ", *pos_nos)

pos_nos = [num for num in list2 if num >= 0]
print("input: ",*list2)
print("output: ", *pos_nos)
