file1 = open("1/input.txt",'r')
lines = file1.readlines()
elfList = [0]
i = 0
for line in lines:
    if line == "\n":
        # New elf count
        i+=1
        elfList.append(0)
    else:
        value = elfList.pop()
        value += int(line)
        elfList.append(value)
elfList.sort()
print(elfList[-1], sum(elfList[-3:]))