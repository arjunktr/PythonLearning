#Problem: given a list of strings S = ['quick', 'brown'], write a function that takes in this list and returns a list of list with ordered repeated permutations. 
#output - [['quick', 'quick'], ['quick', 'brown'], ['brown', 'quick'], ['brown', 'brown']]
#FYI - S can be of any length.



list = ['quick', 'brown']


def perm(start,end=[]):
    if len(start)==0:
        print(end)
    else:
        for i in range(len(start)):
            perm(start[:i]+start[i+1:],end+start[i:i+1])

perm(list)
