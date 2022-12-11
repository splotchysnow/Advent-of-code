# Day Day 11: Monkey in the Middle
from functools import reduce

def main():

    file1 = open('Stella/11/input.txt', 'r')
    Lines = file1.readlines()
    throw_times = [0,0,0,0,0,0,0,0,0,0,0,0]
    items = [[], [], [], [], [], [], [], [], [], [], [], []]
    operations = [[], [], [], [], [], [], [], [], [], [], [], []]
    tests = []
    trues = []
    falses = []
    Monkey_num = 0
    for x in range(len(Lines)):
        cmd = Lines[x].strip('\n').split()
        if len(cmd) > 0:
            if(cmd[0]=='Monkey'):
                x+=1
                its = Lines[x].strip('\n').replace(',', '').split()[2:]
                for i in its:
                    items[Monkey_num].append(int(i))
                
                x+=1
                ops = Lines[x].strip('\n').replace(',', '').split()[3:]
                operations[Monkey_num] = ops
                

                x+=1
                tests.append(int(Lines[x].strip('\n').replace(',', '').split()[3]))
                
                x+=1
                trues.append(int(Lines[x].strip('\n').replace(',', '').split()[5]))
                
                x+=1
                falses.append(int(Lines[x].strip('\n').replace(',', '').split()[5]))
                
                Monkey_num += 1

    result1 = 1
    print(tests)
    for x in tests:
        result1 = result1 * x
    print(result1)

    for rounds in range(10000):
        for iter in  range(8):
            throw_times[iter] += len(items[iter])
            for item in items[iter]:
                old = item
                if operations[iter][0] == 'old':
                    n1 = old
                else:
                    n1 = int(operations[iter][0])
                if operations[iter][2] == 'old':
                    n2 = old
                else:
                    n2 = int(operations[iter][2])
                if operations[iter][1] == '+':
                    new = n1 + n2
                else:
                    new = n1 * n2
                new = new%result1
                if new%tests[iter] == 0:
                    items[trues[iter]].append(new)
                else:
                    items[falses[iter]].append(new)
                # print(int(new))
            items[iter].clear()
            # print(items)

    # print(items)
    # print(operations)
    # print(tests)
    # print(trues)
    # print(falses)
    throw_times.sort(reverse=True)
    print(throw_times)
    print(throw_times[0]*throw_times[1])



main()
