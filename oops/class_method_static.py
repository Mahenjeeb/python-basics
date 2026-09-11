# classmethod
# --------------
# Can access class variable and methods using 'cls' parameter
# Other parameter will be the value coming from arguments example - noOfDogs(cls, text)
# __init__ is just one way to create an object. But in real code, 
# you often need multiple ways to build the same thing
# classmethods are just "another door into the same object" — and cls makes sure the right subclass gets built.
# -----------------------------
# classmethod vs staticmethod
# ---------------------------
# accesing classmethod doen not need new instance of class (same as staticmethod)
# staicmethod can't access class variable directly. you can access it by className.variable.
# classmethod can access class variable using 'cls'

class Dog:
    dogs = []
    @classmethod
    def noOfDogs(cls):
        return len(cls.dogs)
    @classmethod
    def dogFoodCheckList(cls, txt):
        return [food.strip() for food in txt.split("-")]
    @classmethod
    def dogDetails(cls):
        print(f"Number Of Dogs {len(cls.dogs)}")
    
print(Dog.noOfDogs())
print(Dog.dogFoodCheckList("Pedigree-Biscuit-Milk"))

class BullDog(Dog):
    pass

print(f"From BullDog {BullDog.noOfDogs}")
print(f"From BullDog {BullDog.dogFoodCheckList("Meat-Fish-Soya")}")
BullDog.dogDetails()
