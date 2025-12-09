#print()
print(10,20,30,40)

# len()
alist = [10,20]
print(len(alist))

# range()
for val in range(1,5):
    print(val)

alist = [10,20,30]
print(max(alist))
print(min(alist))
print(sum(alist))

# id() - display unique value of memory
name = "python"
print(id(name))

# open() - open the file
fobj = open("emp.txt")
print(fobj.read())

#### display all the complete  list of builtin functions
print(dir(__builtins__))

# casting functions - converting from one object to anothr object
name = "python"
print(list(name))
print(tuple(name))
print(set(name))
val = 10
print(float(val))
print(oct(val))