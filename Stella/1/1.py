from time import time
  
  
def timer_func(func):
    # This function shows the execution time of 
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func

@timer_func
def main():

    file1 = open('1/input.txt', 'r')
    Lines = file1.readlines()
    
    # print(Lines)
    #Strips the newline character
    whole = []
    single = []
    index = 0
    maxs = [0,0,0]
    current = 0

    for line in Lines:
        if not line=='\n':
            current+=int(line.strip('\n'))

        else:
            index += 1
            if current>min(maxs):
                maxs[maxs.index(min(maxs))] = current
            current = 0

    print("Those Elves carryies " + str(sum(maxs)) + ' Calories in total.')
    # print("The "+ str(maxIndex) +'th elf carryies the most Calories which is ' + str(max) + ' Calories.')

main()