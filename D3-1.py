import string

# read file input and split into 2 (done)
# priority_value={a:1, b:2, ... } (done)
# count the value only if it reappears  in the second half (done)
# create a list of compartment 1 ={} (done)
# for each row, the length = len(row#)/2 (done)
# need to update the whole input data

filename = 'test_input.txt'    
with open(filename, 'r') as fin:
    for line in fin:
        rucksack = [x for x in line.strip()]
        # compartment_count
        c = int(len(rucksack) / 2)
        print(c)
        # split the dict into two parts
        # part1 = slice(c)
        # part2 = slice(c, 2*c+1)

        compartment1 = rucksack[slice(c)]
        compartment2 = rucksack[slice(c, 2 * c + 1)]

        # for sub in compartment2:
        # if sub not in compartment2:
        #     compartment2_new

        print(rucksack)
        print(compartment1)
        print(compartment2)
        priority_item = {}
        sum = []

    for x in compartment2:
        if x in compartment1:
            priority_item[x] = 1
            print(priority_item)

            #Todo: Find the Sum of the priority values(currently stuck at this sum.)
            # if x == string.ascii_lowercase:
            #     p_map1 = dict(zip(string.ascii_lowercase, range(1, 27)))
            #     p_value = p_map1[x]
            #     print(p_value)
            #     sum(p_value)
            #     print(sum)
            # else:
            #     p_map2 = dict(zip(string.ascii_uppercase, range(27, 53)))
            #     p_value = p_map2[x]
            #     print(p_value)
            #     sum.append(p_value)
            #     print(sum)
            # break








