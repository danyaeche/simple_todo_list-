class Todo_list(object):
	def __init__(self):
		self.items_dict = {}
		self.counter = 0 

	def add_item(self, item):
		if type(item) != str: 
			print("input item has to be a string") 
		elif item in self.items_dict:
			pass
		else: 
			self.counter += 1 
			self.items_dict[item] = self.counter 

	def edit_item(self, item, new_item):
		if item in self.items_dict:
			self.items_dict[new_item] = self.items_dict.pop(item)
		else:
			print("Item is not in todo_list") 
	
	def delete_item(self, item):
		if item in self.items_dict:
			del self.items_dict[item]
		else:
			print("Item is not placed in the list")

	def return_length(self):
		return len(self.items_dict)
 

	def delete_n_item(self, n):
		if n <= len(self.items_list):
			for key, val in self.items_dict.items:   
                        	if val == n:  
                                	del self.items_dict[key]
		else:
			print("item doesn't exist in to do list")
 

	def delete_select_items(self, delete_list):
		for x in delete_list: 
			for key, val in self.items_dict.items:   
                        	if key == x:
                                	del self.items_dict[key]

	def sort_list(self):
		sorted_items_list = sorted(self.items_dict.items(), key=lambda x: x[1])
		self.items_dict = sorted_items_list

  
		
