# Day 9: Rope Bridge
class Point:
    visited = False
    def _init_(self):
        self.visited = False
    def printPoint(self):
        if(self.visited):
            return('#')
        else:
            return('.')
    def visit(self):
        self.visited = True


class Person:
    hx = 0
    hy = 0
    tx = 0
    ty = 0
    def U(self):
        self.hy+=1
    def R(self):
        self.hx+=1
    def D(self):
        self.hy-=1
    def L(self):
        self.hx-=1
    def check(self):
        if abs(self.hy-self.ty) + abs(self.hx-self.tx) > 2:
            if self.hx > self.tx:
                self.tx+=1
            else:
                self.tx-=1
            if self.hy > self.ty:
                self.ty+=1
            else:
                self.ty-=1
            return [self.tx, self.ty]    
        elif abs(self.hy-self.ty) > 1:
            self.ty = (self.hy+self.ty)/2
            return [self.tx, self.ty]
        elif abs(self.hx-self.tx) > 1:
            self.tx = (self.hx+self.tx)/2
            return [self.tx, self.ty]  
        else: 
            return False
    def Pos(self):
        return [self.hx, self.hy, self.tx, self.ty]


# y
# ^
# |
# --->x
# print [0][4], [1][4], ....
class Grid:
    p = Person()
    y_int =  [Point() for i in range(5)]
    grid = [y_int, y_int, y_int, y_int, y_int, y_int]
    def _init_(self):
        return 0
    def printGrid(self):
        position = self.p.Pos()
        print(position)
        for y in range (len(self.grid[0])):
            line = ''
            for x in range(len(self.grid)):
                if x == position[0] and (4-y) == position[1]:
                    line += 'H'
                elif x == position[2] and (4-y) == position[3]:
                    line += 'T'
                else:
                    line += self.grid[x][4-y].printPoint()
            print(line)
    def getPerson(self):
        return self.p
    def update(self):
        tail = self.p.check()
        # print(tail)
        # try:
        #     self.grid[tail[0]][tail[1]].visit()
        # except:
        #     return 

def main():

    file1 = open('Stella/9/input.txt', 'r')
    Lines = file1.readlines()
    grid = Grid()
    grid.printGrid()

    for line in Lines:
        cmd = line.split()
        call = getattr(grid.getPerson(), cmd[0])
        for x in range(int(cmd[1])):
            call()
            grid.update()
        print(cmd)
        print(grid.getPerson().Pos())
        grid.printGrid()


   


main()
