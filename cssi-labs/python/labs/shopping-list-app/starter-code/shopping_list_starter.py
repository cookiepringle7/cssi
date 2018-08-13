#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

choice = ""

print("\nWelcome to the shopping list app!")



list1 = ['banana','apples','cherries','steak','bacon','chicken','broccolli','corn']

if choice == "5":
    print ("Program Terminated")

while choice.lower() != "5":
    print list1
    print("\nPlease choose your action from the following list:\n")
    print("1. Add an item to the list")
    print("2. Remove an item from the list")
    print("3. Check to see if an item is on the list")
    print("4. Show all items on the list")
    print("5. Exit\n")

    choice = raw_input("\nEnter your choice [1|2|3|4|5]:")

    # Your code below! Handle the cases when the user chooses a, b, c, d, or e

    if choice == "1":
        v = raw_input("input item to add\n")
        list1.append(v)
        print list1

    elif choice == "2":
        o = raw_input("intput item to remove\n")
        list1.remove(o)
        print list1


    elif choice == "3":
        print list1
        p = raw_input("input item to check\n")
        if p in list1:
            print("the item is there")
        else:
            print("item is not there")


    elif choice == "4":
        for i in list1:
            print i
