class Todo_list_v2(object):
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

  def delete_item(self, item):
    if item in self.items_dict:
      del self.items_dict[item]
    else: 
      print("item doesn't exist in list")

  def edit_item(self, item, new_item):
    if item in self.items_dict: 
      temp_counter = self.items_dict[item]
      del self.items_dict[item]
      self.items_dict[new_item] = temp_counter
    else:
      print("item is not in the list")

  def get_length(self):
    return (len(self.items_dict))
   
  def add_n_items(self, items_list):
    for x in items_list:
      self.add_item(x)

  def delete_n_items(self, items_list):
    for x in items_list:
      self.delete_item(x)

  def sort_items(self, bool_flag):
    if bool_flag == False:
      self.items_dict = {k: v for k, v in sorted(self.items_dict.items(), key=lambda item: item[1])}
    else:
      self.items_dict = {k: v for k, v in sorted(self.items_dict.items(), key=lambda item: item[0])} 

    return self.items_dict
    