from todo_list_v2 import Todo_list_v2

def main():
  print("A simple todo list")
  todo_list_v2 = Todo_list_v2()

  todo_list_v2.add_item("first item")
  todo_list_v2.add_item(5)
  todo_list_v2.add_item("first item")
  print(todo_list_v2.items_dict)
  print(todo_list_v2.counter)

  todo_list_v2.delete_item("first item")
  todo_list_v2.delete_item("first item")
  print(todo_list_v2.items_dict)
  
  todo_list_v2.add_item("first item")
  print(todo_list_v2.items_dict)
  todo_list_v2.edit_item("first item", "first_editied_item")
  print(todo_list_v2.items_dict)
  todo_list_v2.edit_item("second item", "first_editied_item")

  print(todo_list_v2.get_length)

  todo_list_v2.sort_items(False)

  todo_list_v2.add_n_items(["second item", "third item", 5,  "fourth item", 2.44])
  print(todo_list_v2.items_dict)

  print(todo_list_v2.sort_items(False))
  print(todo_list_v2.sort_items(True))

  todo_list_v2.delete_n_items(["second item", "third item", 5,  "fourth item", 2.44])
  print(todo_list_v2.items_dict)

if __name__== '__main__':
	main()
