class Car:
    # __init__ used for consturctor
    # type with _ is used to distinguish between inbuilt type()
    def __init__(self, type_, brand):
        self.type = type_
        self.brand = brand
    def displayCarDetails(self):
        print(f"Car is {self.brand} of type {self.type}")
        
carObj = Car("Sedan","Mercedez")
carObj.displayCarDetails()

class Police:
    def __init__(self, pos, rank):
        self.pos = pos
        self.rank = rank
    def policeOfficerDetails(self):
        print(f"Police Office postion is {self.pos} and rank is {self.rank}")

police_instance_01 = Police("IAS","Top Tier")
police_instance_02 = Police("SP","High Tier")

police_instance_01.policeOfficerDetails()
police_instance_02.policeOfficerDetails()