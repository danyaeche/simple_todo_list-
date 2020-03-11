class Todo_list_v3(object):
  def __init__(self):
    self.items_list = []

  '''
  def __str__(self):
    return "items_list = " + self.items_list
  '''

  '''
  Method to add item into to the list checks for if the 
  value type is a string
  '''
  def add_item(self, item):
    if type(item) != str:
      return TypeError
    elif item in self.items_list:
      pass
    else:
      self.items_list.append(item)

  '''
  Method to delte an item in a list check if value is in the
  list first
  '''
  def delete_item(self, item):
    try:
      self.items_list.remove(item)
    except ValueError: 
      return ValueError

  '''
  Method to edit preexisting items in the list
  '''
  def edit_item(self, item, new_item):
    x = -1
    for i in range(self.items_list):
      if self.items_list[i] == item:
        x = i
    if x == -1:
      raise ValueError
    else:
      self.items_list[x] = new_item

  '''
  Method to return the length of the list 
  '''
  def get_length(self):
    return (len(self.items_dict))

  '''
  Method to add multiple items in the list
  '''
  def add_n_items(self, items_list):
    for x in items_list:
      self.add_item(x)

  '''
  Method to delete multiple items in the list
  '''
  def delete_n_items(self, items_list):
    for x in items_list:
      self.delete_item(x)

  '''
  Method to sort item in the list lexigraphically in the list 
  '''
  def sort_items(self, bool_flag):
    sorted_item_list = sorted(self.items_list)
    return sorted_item_list 