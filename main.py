from todo_list_v3 import Todo_list_v3

def main():
  print("A simple todo list")
  todo_list_v3 = Todo_list_v3()

  todo_list_v3.add_item("event-a")
  print(Todo_list_v3[0])
  

  


if __name__== '__main__':
	main()
