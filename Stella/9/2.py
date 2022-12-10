# Day 6: Tuning Trouble


def main():

    file1 = open('Stella/6/input.txt', 'r')
    Lines = file1.readlines()
    nums = ['0','0','0','0','0','0','0','0','0','0','0','0','0','0']
    count = 0
    s = {set}
    for line in Lines:
        # print(len(line))
        for ch in line:
            count += 1
            nums[count%14] = ch
            for x in nums:
                if(x.isalpha()):
                    s.add(x)
            # print(s)
            if(len(s)==14):
                print(count)
                break
            else:
                s.clear()


main()
