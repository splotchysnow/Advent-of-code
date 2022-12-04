# Day 4: Camp Cleanup

def main():

    file1 = open('Stella/4/input.txt', 'r')
    Lines = file1.readlines()
    
    contains = 0

    for line in Lines:
        pairs = line.strip('\n').split(',')
        first = set(range(int(pairs[0].split('-')[0]), int(pairs[0].split('-')[1])+1))
        second = set(range(int(pairs[1].split('-')[0]), int(pairs[1].split('-')[1])+1))
        if (first.issubset(second) or second.issubset(first)):
            contains += 1

    print(str(contains) + ' pairs fully contain the other')

main()
