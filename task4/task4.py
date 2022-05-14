from sys import argv
script, filename = argv
file = open(filename, "r")
array = []
while True:
    line = file.readline()
    if not line:
        break
    array.append(int(line))
array.sort()
num = ""
length = len(array)
if length % 2 == 0:
    place1 = length//2 -1 
    place2 = length//2
    middle1_dif =  array[place1] - array[0]
    middle2_dif = array[place2] - array[-1]
    if abs(middle1_dif) > abs(middle2_dif):
        num = array[place2]
    else:
        num = array[place1]
else:
    num = array[(length - 1) // 2]
result = 0
for i in array:
    result += abs(num - i)
print(result)
    
