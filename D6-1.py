from collections import deque

# check the count
# use a deque

# add a letter one by one to the deque
# from the fourth, check whether characters are all different
# if the last
# the search stops when all the four letters are different
# increase the count for every append c =+1
# c=0, last_four = deque([])

filename = 'D6-1_input_p.txt'
c = 0
last_four = deque([])

with open(filename, 'r') as fin:
    while True:
        cha = fin.read(1)
        # print(cha)
        c += 1
        last_four.append(cha)
        # print(f"c={c}")
        # print(last_four)
        

        if last_four.count == 4:
            if len(set(last_four)) ==4:
                print(f"c={c}")
                print(c)
                break
        if c > 4:
           last_four.popleft()
           print(last_four)
           if len(set(last_four)) == 4:
               print(last_four)
               print(c)
               break
