class Child:
    no_of_toffees=80
    total_toffees_eaten=2
    
    def __init__(self,name):
        self.name=name
        Child.add_toffee(len(self.name))
        Child.total_toffees_eaten+=2
    
    def eat_toffee(self,num):
        Child.no_of_toffees-=num
        Child.total_toffees_eaten+=num
        
    @staticmethod
    def add_toffee(num):
        Child.no_of_toffees+=num//2
child_one=Child("Helen")
child_two=Child("Troy")
child_one.eat_toffee(2)
Child.add_toffee(6)
child_one.add_toffee(3)
child_two.eat_toffee(4)
print("Total toffees left",Child,no_of_toffees)
print("Total toffees eaten",Child.total_toffees_eaten)


##Output##
# Total toffees left <class '__main__.Child'> 80
# Total toffees eaten 12
