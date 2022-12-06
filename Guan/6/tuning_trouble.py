# get input:
file1 = open("Guan/6/input.txt",'r')
lines = file1.readlines()

array_list = []

def import_character(character,array_list,size):
    if (len(array_list) == size):
        array_list.pop(0)
    array_list.append(character)

def isKey(list_,size):
    if (len(list_) == size):
        set_ = set()
        for item in list_:
            set_.add(item)
        # print(set_)
        if (len(set_) == size):
            return True
        else:
            return False
    return False

counter = 0
for characters in lines:
    for character in characters:
        import_character(character,array_list,14)
        print(array_list)
        counter += 1
        if (isKey(array_list,14)):
            print("Character key is:", counter) # Part 1 : answer 1198
            break