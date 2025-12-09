##### string
name = "python"
if "th" in name:
    print("substring exists")


if name.islower():
    print("its lower")

####### list###########
alist = [10,20,30]
if 30 in alist:
    print("value exists")

if len(alist)  == 3 :
    print("total length is 3")

######## dictionary : validating whether key is existing or not
book = {"chap1":10 ,"chap2":20}
if "chap1" in book:
    print("key exists")

if "chap1" in book.keys():
    print("key exists")