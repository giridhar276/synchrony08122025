alist = [10,45,67,32,65,28,92]
print(alist)
#list.append(val) - add single value at the end of the list
alist.append(59)          
print("After appending:",alist)
 # list.extend(list) - add multiple values
alist.extend([96,39,31]) 
print("After extending:",alist)
# list.insert(index,value) - insert at any location with index
alist.insert(1,450)
print("After inserting:",alist)  
val_count= alist.count(45)
print("count:", val_count)

#list.pop(index) : value that index will removed
alist.pop(0)
print("After pop operation :",alist)

alist.remove(65)
print("After remove opeation:",alist)

alist.reverse()
print("After reversing :",alist)

alist.sort()
print("sorting in ascending order:",alist)