    # # some simple testing:
    # line_1 = lines[0]
    # # remove the \n first
    # line_1 = line_1.replace("\n", "")

    # print(line_1.split(","))
    # for string_ in line_1.split(","):
    #     print(string_.split("-"))

# check if the two list contains interger overlap COMPLETE OVERLAPS checking direction a- includes ->b
def check_overlap(a:list, b:list):
    if (a[0] <= b[0] and a[1] >= b[1]):
        return True
    else:
        return False

def check_not_overlap(a:list, b:list):
    if (a[1] < b[0] or a[0] > b[1]):
        return True
    else:
        return False


def main():
    file1 = open("Guan/4/input.txt",'r')
    lines = file1.readlines()

    list_ = []
    for line in lines:
        #remove the dash n.
        line = line.replace("\n", "")
        # split the line by the middle
        new_list = line.split(",")
        # now I should have two different lines.
        list_.append(new_list[0].split("-"))
        list_[-1] = [int(x) for x in list_[-1]]
        
        list_.append(new_list[1].split("-"))
        list_[-1] = [int(x) for x in list_[-1]]

    count = 0
    overlap_counter = 0
    for i in range(int(len(list_)/2)):
        first_list = list_[i*2]
        second_list = list_[i*2+1]
        checker = check_overlap(first_list, second_list)
        no_overlap = check_not_overlap(first_list,second_list)
        
        if checker:
            count+=1
        # also check the other way around:
        else:
            checker = check_overlap(second_list, first_list)
            if checker:
                count +=1
        if(not no_overlap):
            overlap_counter += 1
        print(first_list, second_list, not no_overlap)
    # print(count)
    print(overlap_counter)


main()

