

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
    file1 = open("1/input.txt",'r')
    lines = file1.readlines()
    elfList = [0]
    i = 0
    for line in lines:
        if line == "\n":
            # New elf count
            i+=1
            elfList.append(0)
        else:
            value = elfList.pop()
            value += int(line)
            elfList.append(value)
    elfList.sort()
    print(elfList[-1], sum(elfList[-3:]))

main()