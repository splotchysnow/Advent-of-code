# Day 10: Cathode-Ray Tube

# returns count based on if the Point is already visited
class Register:
    X = 1
    cycles = -1
    result = ''
    def _init_(self):
        self.X = 1
        self.cycles = 0
    def addx(self, num):
        pos = [self.X % 40, (self.X-1) % 40, (self.X+1) % 40]
        self.cycles += 1
        if self.cycles%40 in pos:
            self.result += '#'
        else:
            self.result += ' '
        self.cycles += 1
        if self.cycles%40 in pos:
            self.result += '#'
        else:
            self.result += ' '
        self.X += num
    def noop(self):
        self.cycles += 1
        pos = [self.X % 40, (self.X-1) % 40, (self.X+1) % 40]
        if self.cycles%40 in pos:
            self.result += '#'
        else:
            self.result += ' '
    def getImage(self):
        print(self.result[:40])
        print(self.result[40:80])
        print(self.result[80:120])
        print(self.result[120:160])
        print(self.result[160:200])
        print(self.result[200:240])



def main():

    file1 = open('Stella/10/input.txt', 'r')
    Lines = file1.readlines()
    reg = Register()
    for line in Lines:
        cmd = line.strip('\n').split()
        if(len(cmd)==2):
            reg.addx(int(cmd[1]))
        else:
            reg.noop()
    reg.getImage()

main()
