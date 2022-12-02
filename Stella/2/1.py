# Day 2: Rock Paper Scissors
shapeScore = {
  'X': 1,
  'Y': 2,
  'Z': 3
}

# X for Rock, Y for Paper, and Z for Scissors.
# A for Rock, B for Paper, and C for Scissors.
outScore = {
    'X' : { 'A': 3, 'B': 0, 'C': 6}, 
    'Y' : { 'A': 6, 'B': 3, 'C': 0},
    'Z' : { 'A': 0, 'B': 6, 'C': 3},
}

def main():


    file1 = open('Stella/2/input.txt', 'r')
    Lines = file1.readlines()
    
    # print(Lines)
    #Strips the newline character
    total = 0

    for line in Lines:
        x = line.strip('\n').split(' ')
        total += shapeScore[x[1]] + outScore[x[1]][x[0]]

    print('Total score if everything goes exactly according to my strategy guide is ' + str(total))
    # print('The '+ str(maxIndex) +'th elf carryies the most Calories which is ' + str(max) + ' Calories.')

main()
