# A rock B paper C scissor
# X rock Y Paper Z scissor
winning_dict = {"A":"Y","B":"Z","C":"X"}
loosing_dict = {"A":"Z","B":"X","C":"Y"}
points_dict = {"X":1,"Y":2,"Z":3}
tie_dict = {"A":1,"B":2,"C":3}

file1 = open("Guan/2/input.txt",'r')
lines = file1.readlines()

enemyChoice = []
ourChoice = []

# print(winning_dict["B"])


# Segregate the choices into each list.
for line in lines:
    enemyChoice.append(line[0])
    ourChoice.append(line[2])
    
# print(enemyChoice)
# print(ourChoice)

def part1():
    total_won = 0

    # 1 for rock, 2 for paper and 3 for scissor
    # 0 if you loose 3 if the round is draw and 6 if you won.
    for i in range(len(ourChoice)):
        value = 0 # Reset value
        value += points_dict[ourChoice[i]]
        # i represents the index value of the rounds!
        if(ourChoice[i] == winning_dict[enemyChoice[i]]):
            # we win:
            value += 6
            total_won += value
            
        elif(ourChoice[i] == loosing_dict[enemyChoice[i]]):
            # we loose:
            value += 0
            total_won += value
        else:
            # we tied.
            value += 3
            total_won += value

    print(total_won)

def part2():
    total_won = 0
    # 1 for rock, 2 for paper and 3 for scissor
    # 0 if you loose 3 if the round is draw and 6 if you won.
    for i in range(len(ourChoice)):
        value = 0 # Reset value
        # i represents the index value of the rounds!
        if(ourChoice[i] == "Z"):
            # we win:
            value += 6
            value += points_dict[winning_dict[enemyChoice[i]]]
            total_won += value
            
        elif(ourChoice[i] == "X"):
            # we loose:
            value += 0
            value += points_dict[loosing_dict[enemyChoice[i]]]
            total_won += value
        else:
            # we tied.
            value += 3
            value += tie_dict[enemyChoice[i]]
            total_won += value

    print(total_won)

part2()