class Parent:
    def __init__(self, prop, cash):
        self.prop = prop
        self.cash = cash
    def printPar(self):
        print(f"From Parent {self.prop} - {self.cash}")
        
class Child(Parent):
    def printChild(self):
        print("From Child")
        
class GrandChild:
    pobj = Parent
    def __init__(self):
        self.pr = self.pobj("Stock", "$900000")
    def prGch(self):
        print(f"Grand Child shows parent {self.pr.prop} and {self.pr.cash}")

class GGChild(GrandChild):
    pobj = Child
 
gchildObj = GrandChild()
gchildObj.prGch()

ggChObj = GGChild()
ggChObj.pr.printChild()