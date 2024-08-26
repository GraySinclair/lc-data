# lists
food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
splitfood = food.split(",")
splitfood.sort()

splitequipment = equipment.split(",")
splitequipment.sort()

splitpets = pets.split(",")
splitpets.sort()

splitsleepaids = sleep_aids.split(",")
splitsleepaids.sort()

# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.
cargo_hold = []
cargo_hold.append(splitfood)
cargo_hold.append(splitequipment)
cargo_hold.append(splitpets)
cargo_hold.append(splitsleepaids)

# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.
userinput = int(input("Select a cabinet (0 - 3) in the cargo_hold: "))


# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.
if userinput not in range(4):
    print("Please only select a number between (0 - 3)! Now restart the program!")
else:
    print(cargo_hold[userinput])

itemselect = input("Please select an item: ")

if itemselect in cargo_hold[userinput]:
    dn = "DOES"
else:
    dn = "DOES NOT"

# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”

print("Cabinet {} {} contain {}.".format(userinput, dn, itemselect))