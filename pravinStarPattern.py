# 'P' shape star pattern
for row in range(7):
    for col in range(5):
        if (col==0) or ((col>0 and col<4) and (row==0 or row==3)) or ((col==4) and (row==1 or row==2)):
            print("*",end="")
        else:
            print(end=" ")
    print()

print("\n")
# 'R' shape star pattern
for row in range(7):
    for col in range(5):
        if ((row==0 or row==3) and col!=4) or ((col==0 or col==4) and (row!=0 and row!=3)):
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

# 'V' shape star pattern
for row in range(4):
    for col in range(7):
        if ((col==0 or col==6) and row==0) or ((col==1 or col==5) and row==1) or ((col==2 or col==4) and row==2) or (col==3 and row==3):
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


# 'N' shape star pattern
for row in range(7):
    for col in range(7):
        if (col==0) or (col==6) or (col==1 and row==1) or (col==2 and row==2) or (col==3 and row==3) or (col==4 and row==4)  or (col==5 and row==5):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n")
