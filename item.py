class item:
  def __init__(self):
    self.item = []
  
  def add(self, itemName):
    self.item.append(itemName)

  def remove(self, itemName):
    self.item.remove(itemName)
  
  def replace(self, replaceItem, replacedItem):
    for index, item in self.item:
      if item == replaceItem:
        self.item[index] = replacedItem
  
  def show(self):
    return self.item
