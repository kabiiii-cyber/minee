
class employee:
  def __init__(self,name,position,salary):
    self.name = name
    self.position = position
    self.salary = salary



    #behavior

    def details(self):
      print(self.name,"is the",self.position)





employee1 = employee("john","CEO","400000")
print(employee1.name,employee1.position,employee1.salary)

employee2 = employee("jane","hr","300000")
print(employee2.name,employee2.position,employee2.salary)


employee3 = employee("james","manager","55200")
employee4 = employee("eunice","pa","20000")
