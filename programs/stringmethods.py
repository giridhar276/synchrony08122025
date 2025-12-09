
#p    y    t    h     o     n         p     r     o      g    r    a    m    m   i    n    g
#0    1    2    3     4     5   6    7      8      9    10   11    12   13  14   15  16   17

name = "python programming"
print(name)
########### slicing ##########
# string[start:stop:step]
print(name)
print(name[0]) #p
print(name[1]) # y
print(name[0:4])  #pyth
print(name[0:9])  #python pr
print(name[8:10])
print(name[0:4])
print(name[0:10])
print(name[0:10:1])
print(name[0:10:2])
print(name[::])  # python programming
print(name[::-1])  # string reverse
######## concatenation ###########
first = "python"
second = "programming"
final = first + second
print(final)



name = "python programming"
print(name.capitalize())

print(name.capitalize())

print(name.title())
print(name.replace("python","java"))
print(name)  # we are not modifying actual string..we are just dsiplaying

print(name.startswith("p"))
print(name.endswith("z"))

print(name.count("p"))
print(name.count("z"))

# wil check for substrinr
print(name.find("tho"))  # if substring is found.. it returns the position of substring
print(name.find("z"))    # if not found.. it returns -1

aname = "   python  "
print(len(aname))
print(len(aname.strip()))  # wil remove whitespaces at both ends
print(len(aname.lstrip())) # only at left side
print(len(aname.rstrip()))

name = "python programming"
print(name.upper().capitalize().lower())
print(name.upper().capitalize().count("p"))
print(name.upper().capitalize().count("P"))


print(name.isalnum())
print(name.isalpha())
print(name.islower())
print(name.isupper())


# simple if 
if 1 < 2 :
    print("true")
    print("inside condition")
    print("still inside condition")

print("regular code")


name = "python"
if name.islower():
    print("string is lower")

if name == "python":
    print("true")

if name.startswith("p"):
    print("its python")


# check for substring
if 'p' in name:
    print("substring found")


# this is single lin comment

'''
this is
multiline comment
'''

####### if-else ################
name = input("Enter any langauge:")    # input() is used to read input from the keyboard
if name.islower():
    print("string is lower")
    print("inside if")
    print("still inside if")
else:
    print("string is upper")


# check for substring
name  = "python"
if "p" in name:
    print("substring found")
else:
    print("not found")


#### if-elif-elif-elif-elif-else
lang = input("Enter any language:")
if lang == "python":
    print("its python")
elif lang == "unix":
    print("its unix")
elif lang == "java":
    print("its java")
else:
    print("its something else")



# for loop
name = "python"
for i in name:
    print(i)

alist = [10,20]
for val in alist:
    print(val)


name = "python"
for i in name:
    print(i, end =" " )




