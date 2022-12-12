# Day 12: Hill Climbing Algorithm


def findMin(grid, steps, start, end, current, walked):
    if steps[current[0]][current[1]] > walked:
        steps[current[0]][current[1]] = walked
        if grid[current[0]][current[1]] == 69:
            print(current)
            print(walked)
            return
        else:
            try:
                if not grid[current[0]+1][current[1]] - grid[current[0]][current[1]] > 1:
                    findMin(grid, steps, start, end, [current[0]+1, current[1]], walked+1)
            except:
                pass
            try:
                if not grid[current[0]][current[1]+1] - grid[current[0]][current[1]] > 1:
                    findMin(grid, steps, start, end, [current[0], current[1]+1], walked+1)
            except:
                pass
            try:
                if not current[0] == 0:
                    if not grid[current[0]-1][current[1]] - grid[current[0]][current[1]] > 1:
                        findMin(grid, steps, start, end, [current[0]-1, current[1]], walked+1)
            except:
                pass
            try:
                if not current[1] == 0:
                    if not grid[current[0]][current[1]-1] - grid[current[0]][current[1]] > 1:
                        findMin(grid, steps, start, end, [current[0], current[1]-1], walked+1)
            except:
                pass
    else:
        return
    

def main():
    file1 = open('Stella/12/input.txt', 'r')
    Lines = file1.readlines()
    grid = []
    steps = []
    start = []
    end = []
    for x in range(len(Lines)):
        grid.append([])
        steps.append([])
        for char in range(len(Lines[x].strip('\n'))):
            if Lines[x].strip('\n')[char] == 'S':
                start.append(x)
                start.append(char)
            elif Lines[x].strip('\n')[char] == 'E':
                end.append(x)
                end.append(char)
            grid[x].append(ord(Lines[x].strip('\n')[char]))
            steps[x].append(10000)
    grid[start[0]][start[1]] = 10000
    curr = start
    # grid, steps, start, end, current, walked
    findMin(grid, steps, start, end, curr, 0)



    # print(grid)
    # print(steps)
    # print(ord('S'), ord('E'))
    # print(start, end)

        

main()
