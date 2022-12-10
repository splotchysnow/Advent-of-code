# Day 6: Tuning Trouble

# returns count based on if the Point is already visited
class Point:
    def _init_(self):
        self.visited = False
    def visit(self, count):
        if self.visited == False:
            count+=1
        self.visited = True
        return count


def main():

    file1 = open('Stella/9/input.txt', 'r')
    Lines = file1.readlines()
    vv = [Point,Point,Point,Point,Point]
    visited = [vv,vv,vv,vv,vv,vv]
    print(visited[5][4])
    print(visited[5][4].visit(0,0))
    
    # for line in Lines:
   


main()
