
#'S' shapw star pattern
for row in range(7):
    for col in range(5):
        if ((col==0) and (row==1 or row==2)) or ((col==4) and (row==4 or row==5)) or ((col>0 and col<4) and (row==0 or row==3 or row==6)):
            print("*",end="")
        else: 
            print(end=" ")
    print()
print("\n")


# 'A' shape star pattern
for row in range(7):
    for col in range(5):
        if ((col == 0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
            print("*",end="")
        else: print(end=" ")
    print()

print("\n")

# 'K' shape star pattern
for row in range(7):
    for col in range(5):
        if (col==0) or (col==4 and(row==0 or row==6)) or (col==3 and (row==1 or row==5)) or (col==2 and (row==2 or row==4)) or (col==1 and row==3):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n")

#'S' shapw star pattern
for row in range(7):
    for col in range(5):
        if ((col==0) and (row==1 or row==2)) or ((col==4) and (row==4 or row==5)) or ((col>0 and col<4) and (row==0 or row==3 or row==6)):
            print("*",end="")
        else: 
            print(end=" ")
    print()
print("\n")

# 'H' shape star pattern
for row in range(7):
    for col in range(5):
        if (col==0) or (col==4) or (row==3):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n")

# 'I' shape star pattern
for row in range(7):
    for col in range(5):
        if (row==0) or (row==6) or ((col==2) and (row!=0 and row!=6)):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n")