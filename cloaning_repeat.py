list1 = [i for i in range(0,9)]
list2 = [i for i in range(10,20)]
print(list1)
print(list2)
list3 = list1 + list2 
print(list3)

list4 = [i for i in list3 for x in (0,1)]
print(list4)

list5 = list4[:]
print(list5)