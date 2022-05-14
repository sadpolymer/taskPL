from sys import argv
from math import sqrt

script, main, cord = argv
main = open(main)
cord = open(cord)
array = []
line_1 = main.readline()
line_1 = line_1.split(" ")
x = float(line_1[0])
y = float(line_1[1])
line_2 = main.readline()
r = float(line_2)

while True:
    line = cord.readline()
    if not line:
        break
    array.append(line.rstrip().split(" "))

def checker(x,y,r,data):
    a = abs(float(data[0]) - x)
    b = abs(float(data[1]) - y)
    gipotenuza = sqrt(a*a + b*b)
    if r > gipotenuza:
        print("1\n")
    elif r==gipotenuza:
        print("0\n")
    else:
        print("2\n")
        
for i in array:
    checker(x,y,r,i)
