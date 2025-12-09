book = {"chap1":10 ,"chap2":20 ,"chap3":30  }
print(book)


# add new key-value 
book["chap4"] = 40
book["chap5"] = 50
book["chap6"] = 60
print(book)

# display value
print(book["chap1"]) #10
print(book["chap2"]) # 20

### display keys
print(book.keys())

### display values 
print(book.values())

## display items(key-value)
print(book.items())

## remove key -value from dictionary
book.pop("chap1") # chap1-10 will be removed
print(book)

# will remove last inserted key-value pair
book.popitem()
print(book)


