# Day 7: No Space Left On Device

from collections import defaultdict

def main():

    file1 = open('Stella/7/input.txt', 'r')
    Lines = file1.readlines()
    
    # parent file
    path = []
    # dict of files
    files = defaultdict(list)
    # dict of file size
    sizes = {}
    for line in Lines:
        # command line
        # print(line[0])
        args = line.split()
        if args[0] == '$':
            if args[1] == 'cd':
                if args[2] == '..':
                    path.pop()
                else:
                    path.append(args[2])
            # pass ls
        else: 
            if(args[0]=='dir'):
                try:
                    files[path[len(path)-1]].append(args[1])
                except KeyError:
                    files[path[len(path)-1]]= args[1]
            else:
                try:
                    sizes[path[len(path)-1]] = sizes[path[len(path)-1]] + args[0]
                except:
                    sizes[path[len(path)-1]] = args[0]
    # print(files)
    # print(sizes)
    while(len(files))>0:
        print('loop')
        print(len(files.copy()))
        print(files)
        for par in files.copy():
            for ch in files[par]:
                if not ch in files.copy():
                    try:
                        # print('try')
                        sizes[par] = sizes[par] + sizes[ch]
                    except:
                        print('ex')
                        sizes[par] = sizes[ch]
                    # print(files[par])
                    # print(len(files[par]))
                    files[par].remove(ch)
                    # print(files[par])
                    # print(len(files[par]))
                # else:
                    # print(len(files))
            if len(files[par]) == 0:
                print('delete')
                print(len(files))
                del files[par]                
                print(len(files))
        
        

main()
