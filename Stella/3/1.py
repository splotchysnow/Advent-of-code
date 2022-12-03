# Day 3: Rucksack Reorganization

def main():

    file1 = open('Stella/3/input.txt', 'r')
    Lines = file1.readlines()
    
    total = 0
    count = 0
    sacks = []

    for line in Lines:
        line = line.strip('\n')
        sacks.append(set(line))
        count += 1
        if count==3:
            print(sacks)
            common = sacks[0].intersection(sacks[1]).intersection(sacks[2])
            count = 0
            # print(common)
            for x in common:
                if(ord(x)<91):
                    # print(ord(x)-38)
                    total += ord(x)-38
                else:
                    total += ord(x)-96
                    # print(ord(x)-96)
            sacks.clear()
    print('The sum of the priorities of the item types that appears in each three-Elf groups are: ' + str(total))

main()
