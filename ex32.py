the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies','2','dimes','3','quarters']

#this first kind of for-loop goes through a list 
for number in the_count:
    print(f"this is count {number}")

#same as above
for fruit in fruits:
    print(f"a fruit of type: {fruit}")

#also we can go through mixed list too
#notice we have to use {} since we don't know what's in it
for i in change:
    print(f"i got {i}")

#we can also build lists, first start with an empty one
element = []
for i in range(0,6):
    print(f"Adding {i} to the list")
    element.append(i)

#now we can print them out too
for i in element:
    print(f"ELEMENT WAS {i}")
