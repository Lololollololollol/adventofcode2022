def find_the_largest_sum():
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
                    # # save the results
                    # log = str(largest_sum)
                    with open('largest_sum_log', '+a') as fout:
                        fout.write(f"{largest_sum}\n")
                    #     fout.write(f"the largest sum so far is {largest_sum} from the {elf_num}'s elf")

                else:
                    print(f"current sum is {current_sum}")
                    # log = str(largest_sum)
                    with open('largest_sum_log', '+a') as fout:
                    #     # fout.write(f"{log}\n")
                        fout.write(f"{current_sum}\n")
                current_sum = 0


def find_the_top_three():
    the_1st = 0
    the_2nd = 0
    the_3rd = 0
    with open('largest_sum_log', 'r') as fin:
        for sum in fin:
            new_record = int(sum.strip())
            if new_record > the_1st:
                the_1st = new_record
                print(f"the_1st is {the_1st}")
            elif the_2nd < new_record < the_1st:
                the_2nd = new_record
                print(f"the_2nd is {the_2nd}")
            elif the_3rd <new_record < the_2nd:
                the_3rd = new_record
                print(f"the_3rd is {the_3rd}")

            #The answer key for part2 is 195625


def main():
    find_the_largest_sum()
    find_the_top_three()

if __name__ == '__main__':
    main()
