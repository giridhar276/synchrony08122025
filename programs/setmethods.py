

aset = {10,10,10,10,20,20,30}
bset = {30,30,30,40,40,50,50}

print(aset)
print(bset)

# add new value to set
aset.add(10)
print("After adding:",aset)

# union
print(aset.union(bset))

# intsersection
print(aset.intersection(bset))

print(aset.difference(bset))   



