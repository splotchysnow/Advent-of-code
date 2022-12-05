# Day 5: Supply Stacks

def main():

    file1 = open('Stella/5/input.txt', 'r')
    Lines = file1.readlines()
    
    stacks = []
    real = []

    count = 0
    i=0
    start = 0

    for line in Lines:
        stacks.append(list(line))
        count+=1
        if line == '\n':
            print('stop')
            for n in range(len(stacks[(len(stacks)-2)])):
                if stacks[(len(stacks)-2)][n].isnumeric():
                    real.append([])
                    for x in range(len(stacks)-1):
                        if(stacks[len(stacks)-2-x][n].isalpha()):
                            real[i].append(stacks[len(stacks)-2-x][n])
                    i+=1
            start = 1
        if start == 1:
            ins = line.split()
            if len(ins)>1:
                for j in range(int(ins[1])):
                    real[int(ins[5])-1].append(real[int(ins[3])-1].pop())
    for x in real:
        print(x.pop())

main()
