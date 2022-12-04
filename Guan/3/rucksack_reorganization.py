

# returns the priority value of string. a-z -> 1-26 and A-z for 27-52
def find_priority(letter:str):
    if letter != "\n":
        if letter == letter.upper():
            return ord(letter) - 38
        else:
            return ord(letter) - 96
    else:
        return 0

# Better Run time:
# find the similarity in both set and return a list of values of the same sets.
def find_similar(string_1:str, string_2:str):
    # Create an empty set.
    set_1, set_2, repeat = set(), set(), set()
    # Dump every character in first string into the set_
    for character in string_1:
        set_1.add(character)
    for character in string_2:
        set_2.add(character)
    for character in set_2:
        old_length = len(set_1)
        set_1.add(character)
        new_length = len(set_1)
        if(old_length == new_length):
            repeat.add(character)    
    return repeat

# Better Run time:
# find the similarity in both set and return a list of values of the same sets.
def find_similar_for_three(string_1:str, string_2:str, string_3:str):
    # Create an empty set.
    set_1, set_2, set_3, repeat_1_2, repeat = set(), set(), set(), set(), set()
    # Dump every character in first string into the set_
    for character in string_1:
        set_1.add(character)
    for character in string_2:
        set_2.add(character)
    for character in string_3:
        set_3.add(character)
    
    #Find the simiarity in set_1 and set_2
    for character in set_2:
        old_length = len(set_1)
        set_1.add(character)
        new_length = len(set_1)
        if(old_length == new_length):
            repeat_1_2.add(character)
    for character in repeat_1_2:
        old_length = len(set_3)
        set_3.add(character)
        new_length = len(set_3)
        if(old_length == new_length):
            repeat.add(character)    
    return repeat

# Horrible runtime: disgarded.
# # find the similarity in both set and return a list of values of the same sets.
# def find_similar(string_1:str, string_2:str):
#     repeat = set()
#     # Dump every character in first string into the set_
#     for character_1 in string_1:
#         for character_2 in string_2:
#             if(character_1 == character_2):
#                 repeat.add(character_1)        
#     return repeat

def split_half(string_:str):
    length_of_line = len(string_)
    first_half = string_[0:int(length_of_line/2)]
    second_half = string_[int(length_of_line/2):length_of_line]
    return first_half, second_half

def main():
    file1 = open("Guan/3/input.txt",'r')
    lines = file1.readlines()

    maximum_priority = 0
    for line in lines:
        first_half, second_half = split_half(line)
        repeat_set = find_similar(first_half,second_half)

        for character in repeat_set:
            maximum_priority += find_priority(character)
        # print(repeat_set, maximum_priority)
    print(maximum_priority)
    
    part_two_maximum = 0
    for i in range(int(len(lines)/3)):
        first_index = 3*i
        seocnd_index = 3*i + 1
        third_index = 3*i + 2

        for i in find_similar_for_three(lines[first_index], lines[seocnd_index], lines[third_index]):
            part_two_maximum += find_priority(i)
    
    print(part_two_maximum)



main()

