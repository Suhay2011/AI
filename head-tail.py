input("Press enter to see answer")
print("[10,20,30] head: ", [10,20,30][0],"tail:", [10,20,30][1:])
print("[5,15,25] head: ", [5,15,25][0],"tail:", [5,15,25][1:])

list=[int(x) for x in input("Enter 3 numbers sperated by spaces- ").split()]
guess=input("What is the head of" + str(list) )
print("head = ", list[0],"tail=", list[1:])
