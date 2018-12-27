#import argv
from sys import argv

#two variable to be typed
script, filename = argv

#txt = file when open
#print it out using print(txt.read()) means read
txt = open(filename)
print(f"here's your file {filename}")
print(txt.read())

#show prompt and wait for input
print("type the filename again:")
#this means record the input
file_again = input(">")
#use input as file name and open it
txt_again = open(file_again)
#and print it out
print(txt_again.read())