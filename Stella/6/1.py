# Day 6: Tuning Trouble


def main():

    file1 = open('Stella/6/input.txt', 'r')
    Lines = file1.readlines()
    nums = ['0','0','0','0']
    count = 0
    s = {set}
    for line in Lines:
        for ch in line:
            count += 1
            nums[count%4] = ch
            for x in nums:
                if(x.isalpha()):
                    s.add(x)

            if(len(s)==4):
                print(count)
                break
            else:
                s.clear()


main()
