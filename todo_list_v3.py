class Todo_list_v3(object):
  def __init__(self):
    self.items = []

  def add_item(self, item):
    '''
    Method to add item into to the list checks for if the 
    value type is a string
    '''
    if type(item) != str:
      raise TypeError("item must be a string" )
    elif item in self.items:
      raise ValueError("item must be unique in the list")
    else:
      self.items.append(item)

  def delete_item(self, item):
    '''
    Method to delte an item in a list check if value is in the
    list first
    '''
    if item in self.items:
      self.items.remove(item)
    else:
      raise ValueError("Item has to be in the list")

  def edit_item(self, item, new_item):
    '''
    Method to edit preexisting items in the list
    '''
    item_index = -1
    for index in range(len(self.items)):
      if self.items[index] == item:
        item_index = index
    if item_index == -1:
      raise ValueError("item is not in the list")
    else:
      self.items[item_index] = new_item

  def add_n_items(self, items_list):
    '''
    Method to add multiple items in the list
    '''
    for x in items_list:
      self.add_item(x)

  def delete_n_items(self, items_list):
    '''
    Method to delete multiple items in the list
    '''
    for x in items_list:
      self.delete_item(x)

  def sort_items(self):
    '''
    Method to sort item in the list lexigraphically in the list 
    '''
    sorted_item_list = sorted(self.items)
    self.items = sorted_item_list