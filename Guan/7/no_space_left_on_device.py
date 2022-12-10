from SpaceTree import SpaceNodes

def is_command(line):
    if line[0] == "$":
        return True
    else:
        return False

def is_cd(line):
    if line[2:4] == "cd":
        return True
    else:
        return False

def is_ls(line):
    if is_command(line) and is_cd(line):
        return False
    elif is_command(line):
        return True
    else:
        return False

def is_dir(line):
    if not is_command(line) and line[0:3] == "dir":
        return True
    else:
        return False

def main():
    file1 = open("Guan/7/input.txt",'r')
    lines = file1.readlines()
    current = None
    current_command = None

    for line in lines:
        if line == "$ cd /":
            print("root have been initiated")
            root = SpaceNodes("/",0,None)
            current = root
        elif is_command(line) and is_ls(line):
            current_command = "ls"
        elif is_command(line) and is_cd(line):
            current_command = "cd"
            # Go to that area:
            line = line.split(" ")
            # TODO Fix:
            current = current.getContains().find(line[2])
        else:
            if current_command == "ls":
                # we are inside each directory
                if is_dir(line):
                    # get every value:
                    line = line.split(" ")
                    # append directory into the current node.
                    current.appendList(SpaceNodes(line[1],0,current,[]))
                else:
                    line = line.split(" ")
                    currentWeight = int(line[0])
                    # add file names into the current node.
                    current.appendList(SpaceNodes(line[1],int(line[0]),current))
                    # update current weight;
                    current.setWeight(currentWeight)
            else:
                # just got initiated.
                pass
        
main()