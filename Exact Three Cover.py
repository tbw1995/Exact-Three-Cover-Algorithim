from itertools import groupby
import random



s = 1,2,8,9,5,0


if len(s) % 3 != 0:
    print('invalid input')
    quit()

c = [[4,5,7],[1,2,8],[5,0,9],[1,2,3],[1,2,4],[1,2,5],[4,5,6],[1,2,7],[1,4,5]]

ss = s

# Sort list to remove
# sets like (1,2,3) and (1,3,2)
# but leave (1,2,3)

c = [next(v) for _, v in groupby(c, sorted)]


# remove sets
# that have
# repeating
# elements

remove = []
for rem in range(0, len(c)):
    if len(c[rem]) != len(set(c[rem])):
        remove.append(c[rem])

for rem_two in range(0, len(remove)):
    if remove[rem_two] in c:
        del c[c.index(remove[rem_two])]

# remove sets
# that have
# elements
# that don't
# exist in S.



remove=[]
for j in range(0, len(c)):
   for jj in range(0, len(c[j])):
        if any(elem not in s for elem in c[j]):
            remove.append(c[j])

for rem_two in range(0, len(remove)):
    if remove[rem_two] in c:
        del c[c.index(remove[rem_two])]


# Remove repeating sets

solutions =[c[x] for x in range(len(c)) if not(c[x] in c[:x])]


c = solutions



length = len(solutions)
ss = s
new = []
s = set()

for l in c:
    if not any(v in s for v in l):
        new.append(l)
        s.update(l)


# while loop to see
# if we can find
# an Exact Three Cover
# in poly-time.

stop = 0
w = 0
while True:

    # Shuffling c randomly
    # to reduce chance of
    # error.
    
    random.shuffle(c)
    

    if len(new) == len(ss) // 3:
        # break if Exact
        # three cover is
        # found.
        #print(new)
        w = w + 1
        print(new, end = '')
        break
        

    # Keep c[0]
    # and append to
    # end of list
    # del c[0]
    # to push >>
    # in list.
    
    c.append(c[0])
    del [c[0]]
    new = []
    s = set()
    stop = stop + 1
    for l in c:
        if not any(v in s for v in l):
            new.append(l)
            s.update(l)

    if len(new) != len(ss)//3:
        if stop == length:
          # Reverse list just
          # to reduce false -/+
          # answer.
          c = list(reversed(c))
          random.shuffle(c)
    if stop >= length * 3:
        break

