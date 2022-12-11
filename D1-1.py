filename = 'D1-1_input.txt'
largest_sum = 0
current_sum = 0
elf_num = 0
with open(filename, 'r') as fin:
    for line in fin:
        if not line == '\n':
            calorie = int(line.strip())
            current_sum = current_sum + calorie
        else:
            elf_num = elf_num+1
            # print(f" the {elf_num}'s elf has..")
            if current_sum > largest_sum:
                largest_sum = current_sum
                print(f"the largest sum so far is {largest_sum} from the {elf_num}'s elf")
            # else:
            #     print(f"current sum is {current_sum}")
            current_sum = 0

