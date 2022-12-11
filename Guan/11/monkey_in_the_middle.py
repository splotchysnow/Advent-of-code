from monkey import Monkey

file1 = open("Guan/11/input.txt",'r')
lines = file1.readlines()

monkeys = []
monkey = []

monkey_object_list = []

for line in lines:
    if line == "\n":
        monkeys.append(monkey)
        monkey = []
    else:
        monkey.append(line)

# print(monkeys[1])

'''
Monkey structure:
-------------------
line 0 give you monkey names:
line 1 give you the monkeys starting items.
line 2 give you the monkeys operation value and number.
line 3 give you the test value. since they are all division, just get the number.
line 4 give you the true statement. get monkey name
line 5 give you the false statement, get monkey name.
'''

# set up all the monkeys.
for monkey in monkeys:
    # remove \n from the monkey.
    monkey[0] = monkey[0].replace(":\n", "")
    monkey[0] = monkey[0].split(" ")
    monkey_name = monkey[0][1]
    # print(monkey_name) # Good it works.

    # remove dash n and commas
    monkey[1] = monkey[1].replace("\n", "")
    monkey[1] = monkey[1].replace(",", "")
    monkey[1] = monkey[1].split(" ")
    starting_items = monkey[1][4:]
    # print(starting_items) # Good it works.

    monkey[2] = monkey[2].replace("\n", "")
    monkey[2] = monkey[2].split(" ")
    operation = monkey[2][6]
    value = monkey[2][7]

    monkey[3] = monkey[3].replace("\n", "")
    monkey[3] = monkey[3].split(" ")
    test = monkey[3][5]
    monkey[4] = monkey[4].replace("\n", "")
    monkey[4] = monkey[4].split(" ")
    true_senario = monkey[4][-1]

    monkey[5] = monkey[5].replace("\n", "")
    monkey[5] = monkey[5].split(' ')
    false_senario = monkey[5][-1]

    monkey_object_list.append(Monkey(monkey_name,starting_items, operation,test,true_senario,false_senario))

print(monkey_object_list)

for i in range(20):
    for monkey in monkey_object_list:
        for items in monkey.starting_items:
            print(items)