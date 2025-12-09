

atup = (45,67,34,45,45,45,45)
getcount = atup.count(45)
print(getcount)

#atup[0] = 450
print(atup)

getindex = atup.index(67)
print(getindex)


### elements inside tuple cannot be modified directly 
## but indirectly we can make changes by casting(converting from one object to object )

atup = (45,67,34)   # tuple
alist = list(atup)  # convert to list to make changes
alist.append(60)    #  making changes
atup = tuple(alist)
print(atup)

name = "python"
print(list(name))
aset = {10,10,10,20,30}
print(aset) #{10,20,30}
print(list(aset)) # [10,20,30]
