from collections import deque

filename = 'D6-1_input_p.txt'
c = 0
last_four = deque([])

with open(filename, 'r') as fin:
    while True:
        cha = fin.read(1)
        c += 1
        last_four.append(cha)
      

        if last_four.count == 14:
            if len(set(last_four)) == 14:
                print(f"c={c}")
                print(c)
                break
        if c > 14:
           last_four.popleft()
           print(last_four)
           if len(set(last_four)) == 14:
               print(last_four)
               print(c)
               break
