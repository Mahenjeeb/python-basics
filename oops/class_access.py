class Peti:
    def __init__(self, type_, features):
        self.type = type_
        self.features = features
        
# Accessing by Duplicating Properties
class Benguli(Peti):
     def __init__(self, type_, features, work):
            self.type = type_
            self.features = features
            self.work = work
            
# Accessing by class Name
class Dhana(Peti):
    def __init__(self, type_, features, work):
        Peti.__init__(self, type_, features)
        self.work = work

# Acccesing using super()
class Sukuta(Peti):
    def __init__(self, type_, features, work):
         super().__init__(type_, features)
         self.work = work