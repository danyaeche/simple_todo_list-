from todo_list_v3 import Todo_list_v3

def main():
  todo_list_v3 = Todo_list_v3()
  print("Welcome to this easy-to-use Todo list")
  print("You have 7 choices")
  print("Select 1: Add an item to the list")
  print("Select 2: Delete an item to the list")
  print("Select 3: Edit an item to the list")
  print("Select 4: Add multiple items to the list")
  print("Select 5: Delete multiple items to the list")
  print("Select 6: Sort the list lexigraphically")
  print("Select 7: to get the length of the list")
  print("Select 8: Display the Todo list")
  print("Select 9: to close the program")
  while(True):
    user_input = input("Pick a number between 1-8, to select a choice:  ")

    if user_input == 1:
      user_item_input = input("type an item to add: ")
      try:
        todo_list_v3.add_item(user_item_input)
      except TypeError:
        print("Item must be a string value")
      except ValueError:
        print("Item can't be in the list already")

    elif user_input == 2:
      user_item_input = input("type an item to delete: ")
      try:
        todo_list_v3.delete_item(user_item_input)
      except ValueError:
        print("Item has to be in the list")

    elif user_input == 3: 
      old_item, new_item = input("type two item: 1: item to edit, 2:   replacement item ").split()
      try:
        todo_list_v3.edit_item(old_item, new_item)
      except ValueError:
        print("Old item has to be in the list")

    elif user_input == 4:
      user_inputs = []
      while(True):
        choice_user_input = input("Type 1 to add an item, Type 0 end adding items: ")
        if choice_user_input == 1:
          user_item_input = input("Type an item to add: ")
          user_inputs.append(user_item_input)
        else:
          try: 
            todo_list_v3.add_n_items(user_inputs)
          except TypeError:
            print("Item must be a string value in the List")
          except ValueError:
            print("Item must be a new item in the list")

    elif user_input == 5:
      user_inputs = []
      while(True):
        choice_user_input = input("Type 1 to delete a item, Type 0 end adding items: ")
        if choice_user_input == 1:
          user_item_input = input("Type an item to delete: ")
          user_inputs.append(user_item_input)
        else:
          try: 
            todo_list_v3.add_n_items(user_inputs)
          except ValueError:
            print("Item must be in item in the list")

    elif user_input == 6:
      todo_list_v3.sort_items() 

    elif user_input == 7:
      print(todo_list_v3.get_length())    

    elif user_input == 8:
      print(todo_list_v3.items)

    else:
      print(todo_list_v3.items)
      break 

if __name__== '__main__':
	main()
