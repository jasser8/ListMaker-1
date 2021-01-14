# Create simple list of items

user_list = []

def add_item():
  global user_list

  item = input("What would you like to add to your list? " + "\n")
  user_list.append(item)

  answer = "Y"
  while answer == "Y" or answer == "y":
    answer = input("Do you want to add item to your list? [Y/N]")
    print("\n")
    if answer == "Y" or answer == "y":
      item = input("Enter item for you list " + "\n")
      user_list.append(item)
    else:
      answer = "N"
    
  list_len = len(user_list)
  print("You have " + str(list_len) + " items in your list.")

  # print(to_do_list) returns ['item1', 'item2', ,,,, 'itemn"] so remove [ & ' and add new line
  for list_item in user_list:
    # end parameter with ", " indicates end of character ends in comma & space; prints items separated by comma
    print(list_item, end=", ")
    # backspace twice & end char no space
    print("\b\b", end="")
    # add new line
    print(" ") 

    # append list to file MyList.txt
    with open("MyList.txt",'a',encoding = 'utf-8') as f:
     f.write(list_item + "\n")

add_item()

