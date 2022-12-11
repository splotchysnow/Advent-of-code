# Day 8: Treetop Tree House

def main():

    file1 = open('Stella/8/input.txt', 'r')
    Lines = file1.readlines()
    grid = []
    l = []
    for i in range(len(Lines[0])):
        l.append(False)
    for i in range(len(Lines)):
        grid.append(l)
    
    for i in range(len(Lines)):
        print(0)

main()
