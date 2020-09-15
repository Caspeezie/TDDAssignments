print("Invited guest list for Yankari Game Reserve camping trip")

#Initial count of guests in a list
guests = []
#The name counter is set at an initial value of empty
name = " "

while name != "DONE" :
    name = input("Enter guest name (enter DONE if no more names) : ")
    #This will increment the newly added name above to the existing list
    guests.append(name)

#This sorts the name in alphabetical order
guests.sort()
#This prints out total guests list
for guest in guests :
    print(guest)
#This is the last mesage printed after successful addition of new names
print("You have been successfully subscribed. Welcome to CLG guest list!")
