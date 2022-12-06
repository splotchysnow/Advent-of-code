# get input:
file1 = open("Guan/5/input.txt",'r')
lines = file1.readlines()

line_counter = 0
for line in lines:
    if line[1] == "1":
        break
    line_counter+=1

amount_of_container = int(len(lines[0]) / 4)
# print(line_counter)
all_dict = {}

# putting all value in the array for dictionarys.
back_ward_counter = line_counter
for i in range(0,line_counter+1):
    back_ward_counter = line_counter - i
    
    # Read the number of sets and set them to sets.
    if i == 0:
        # pass
        for j in range(amount_of_container):
            # print(lines[back_ward_counter][4*j+1])
            all_dict[lines[back_ward_counter][4*j+1]] = []
        # print(all_dict)
    else:
        for j in range(amount_of_container):
            # Get each contained values.
            all_dict[str(j+1)].append(lines[back_ward_counter][4*j+1])
# print(all_dict)

for x, y in all_dict.items():
#   print(x, y)
    for i in range(len(y)):
        if " " in y:
            y.remove(" ")

# print(all_dict)

# now at this point all_dict represents the all value contains everything else.

# try print the value:

for i in range(line_counter+2,len(lines)):
    lines[i] = lines[i].replace("\n", "")
    split_string = lines[i].split(" ")

    # print(split_string[1], split_string[3], split_string[5])
    move_ = split_string[1]
    from_ = split_string[3]
    to_ = split_string[5]
    for number_of_times in range(int(move_)):
        # part 1 answer
        # all_dict[to_].append(all_dict[from_].pop())
        # part 2 answer
        all_dict[to_].append(all_dict[from_].pop(len(all_dict[from_]) + number_of_times - int(move_)))

# print(all_dict)

answer = ""
for x, y in all_dict.items():
    answer += y[-1]
print(answer)
