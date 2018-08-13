
list1 = ['banana','apples','cherries','steak','bacon','chicken','broccolli','corn']
print list1
print ("\nThis weeks food list\n")
print ("What would you like to do with this weeks list?\n")
print ("You can \n1. Add\n2. Remove\n3. Check to see if item is there\n4. Show all items on the list\n5. Exit\n")


choice = raw_input("Enter your choice [1|2|3|4|5|]:").lower()

print list1
print("What would you like to do with this weeks list?\n")

print("You can \n1. Add\n2. Remove\n3. Check to see if item is there\n4. Show all items on the list\n5. Exit\n")

while choice.lower() != "5":


    if choice == "1":
        v = raw_input("input item to add\n")
        list1.append(v)

    elif choice == "2":
        o = raw_input("intput item to remove\n")
        list1.remove(o)


    elif choice == "3":
        p = raw_input("input item to check\n")
        if p in list1:
            print("the item is there")
        else:
            print("item is not there")


    elif choice == "4":
        for i in list1:
            print i




#else choice == "5":
    #answer = raw_input("add item to list\n")

#raw_input[]
#list1.append
