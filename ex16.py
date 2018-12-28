from sys import argv

script, filename = argv

print(f"this is {filename} file")
print(f"we are going to erase {filename}")
print("if you want to continue, hit return")

input('hit enter to continue')

print('in progress')
target = open(filename, 'w')

print(f'truncating the file name {filename} ')
target.truncate()

print(f"now, we are adding something into {filename}")
input1 = input("line1:")
input2 = input("line2:")
input3 = input("line3:")

print(f"adding content to file: {filename}")
target.write(input1)
target.write('\n')
target.write(input2)
target.write('\n')
target.write(input3)
target.write('finish writing...')