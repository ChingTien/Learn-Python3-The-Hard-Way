ten_things = ("apple orange crows telephone light sugar")

print("wait there is no 10 things in that list. Let's fix it")

stuff = ten_things.split(" ")
more_stuff = ["day","night","song","frisbee","corn","banana", "girl","boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("now adding", next_one)
    stuff.append(next_one)
    print(f"there are {len(stuff)} items now.")

print("there we go:", stuff)

print("let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # fancy
print(stuff.pop())
print(' '.join(stuff)) #cool
print('#'.join(stuff[3:5])) #super!