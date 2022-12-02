# Day 2: Rock Paper Scissors
outScore = {
  'X': 0,
  'Y': 3,
  'Z': 6
}

# X for Lose, Y for Draw,  and Z for Win.
# A for Rock, B for Paper, and C for Scissors.
# Socre:1,2,3
shapeScore = {
    'X' : { 'A': 3, 'B': 1, 'C': 2}, 
    'Y' : { 'A': 1, 'B': 2, 'C': 3},
    'Z' : { 'A': 2, 'B': 3, 'C': 1},
}

def main():


    file1 = open('Stella/2/input.txt', 'r')
    Lines = file1.readlines()
    
    total = 0

    for line in Lines:
        x = line.strip('\n').split(' ')
        total += outScore[x[1]] + shapeScore[x[1]][x[0]]

    print('Total score if everything goes exactly according to my strategy guide is ' + str(total))

main()
