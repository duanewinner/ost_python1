#!/usr/local/bin/python3

#while True:
#    try:
#        f1=int(input("Enter FIRST factor (Integer between 1 and 12): "))
#    except ValueError:
#        continue
#    else:
#        if f1 < 1 or f1 > 12:
#            continue
#        else:
#            break
#print
#while True:
#    try:
#        f2=int(input("Enter SECOND factor 2 (Integer between 1 and 12): "))
#    except ValueError:
#        continue
#    else:
#        if f2 < 1 or f2 > 12:
#            continue
#        else:
#            break        
        
#ftable=()
#for x in range(f1):
#    for y in range(f2):
#        ftable=ftable+((x+1,y+1),)


ftable=((1, 1), (2, 2), (12, 13), (4, 4), (99, 98))

for f1, f2 in ftable:
    print("{0:>4d} ={1:>3d} x{2:>3d}".format(f1*f2, f1, f2))
