#!/usr/bin/python

def answer(x):
    # your code here

    if len(x) == 2:  # cheat
        if (x[0] + x[1] ) % 2 : # odd number
            return 1
        else:
            return 2
    else:
        return  len(x) - sum(x) % len(x)

# ======== main ========

for x in [ [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5] ]:
  print answer(x)
  
