class Todo_list_v3(object):
  def __init__(self):
    self.items = []

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
      raise TypeError("item must be a string" )
    elif item in self.items:
      raise ValueError("item must be unique in the list")
    else:
      self.items.append(item)

  '''
  Method to delte an item in a list check if value is in the
  list first
  '''
  def delete_item(self, item):
    if item in self.items:
      self.items.remove(item)
    else:
      raise ValueError("Item has to be in the list")

  '''
  Method to edit preexisting items in the list
  '''
  def edit_item(self, item, new_item):
    item_index = -1
    for index in range(len(self.items)):
      if self.items[index] == item:
        item_index = index
    if item_index == -1:
      raise ValueError("item is not in the list")
    else:
      self.items[item_index] = new_item

  '''
  Method to return the length of the list 
  '''
  def get_length(self):
    return len(self.items)

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
  def sort_items(self):
    sorted_item_list = sorted(self.items)
    self.items = sorted_item_list