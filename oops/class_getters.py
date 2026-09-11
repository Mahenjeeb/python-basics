# '@propety' is used on selected property you want to have ability to 
#  control inputs
#  '_' used to diffrenciate between property and internal storage
#  @property lets you change how a value is stored or computed without breaking
#  anyone who uses it.
class House:
    def __init__(self, type_, _cost):
        self.type = type_
        self.cost = _cost
    @property
    def cost(self):
        return self._cost
    @cost.setter
    def cost(self, value):
        if value <= 0:
            raise ValueError("Value should non negetive or greater than zero")
        self._cost = value
        
house = House('Villa', 900000)
house.cost = 90
print(house.cost)