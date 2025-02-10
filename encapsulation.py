class phone:
  def __init__(self,brand,cost):

    self.brand = brand
    self.cost = cost




  def brand(self):
    return self.brand

  def cost(self):
    return self.cost


my_phone = phone("samsang","150000")
print("brand",my_phone.brand)

print("cost",my_phone.cost)

