class todo_list(object):
	def __init__():
		items_dict = {}
		counter = 0 

	def add_item(item):
		if type(item) != str: 
			print("input item has to be a string") 
		else if item in items_dict:
			pass:
		else: 
			counter += 1 
			items_list[item] = counter 

	def edit_item(item, new_item):
		if item in items_list:
			items_list[new_item] = items_list.pop(item)
		else:
			print("Item is not in todo_list) 

	
	def delete_item(item):
		if item in items_list:
			del items_list[item]
		else:
			print("Item is not placed in the list)

	def return_length():
		return len(items_dict)
 

	def delete_n_item(n):
		if n <= len(items_list):
			for key, val in items_dict.items:   
                        	if val == n:  
                                	del items_dict[key]
		else:
			print("item doesn't exist in to do list")
 

	def delete_select_items(delete_list):
		for x in delete_list: 
			for key, val in items_dict.items:   
                        	if key == x:
                                	del items_dict[key]

	def sort_list():
		sorted_items_list = sorted(items_dict.items(), key=lambda x: x[1])
		items_dict = sorted_item_list
		
