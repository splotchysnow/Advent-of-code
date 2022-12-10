# Day 10: Cathode-Ray Tube

# returns count based on if the Point is already visited
class Register:
    X = 1
    cycles = 0
    outs = [20,60,100,140,180,220]
    total = 0
    def _init_(self):
        self.X = 1
        self.cycles = 0
    def addx(self, num):
        self.cycles += 2
        if(self.cycles in self.outs):
            self.total += self.cycles*self.X
            print(self.cycles, self.X, self.cycles*self.X)
        elif(self.cycles-1 in self.outs):
            self.total += (self.cycles-1)*self.X
            print(self.cycles-1, self.X, self.cycles*self.X)
        self.X += num
    def noop(self):
        self.cycles += 1
        if(self.cycles in self.outs):
            self.total += self.cycles*self.X
            print(self.cycles, self.X, self.cycles*self.X)
    def getVal(self):
        return self.total


def main():

    file1 = open('Stella/10/input.txt', 'r')
    Lines = file1.readlines()
    reg = Register()
    i = 0
    for line in Lines:
        i += 1
        cmd = line.strip('\n').split()
        if(len(cmd)==2):
            reg.addx(int(cmd[1]))
        else:
            reg.noop()
    print(reg.getVal())

main()
