print("**** string ****")
name = "python"
for char in name:
    print(char)

print("**** list ****")
alist = [10,20,30]
for val in alist:
    print(val)

print("**** dict keys ****")
book = {"chap1":10 ,"chap2":20}
for key in book.keys():
    print(key)

print("**** dict values ****")
book = {"chap1":10 ,"chap2":20}
for value in book.values():
    print(value)

print("**** dict items ****")
book = {"chap1":10 ,"chap2":20}
for key,value in book.items():
    print(key,value)

print("****  set  ****")
aset = {10,10,20,30,30}
for val in aset:
    print(val)