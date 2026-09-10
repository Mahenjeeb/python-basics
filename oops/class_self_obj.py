class Lata:
    categoty = "Peti"
    def hello():
        print(f"My Name is Lata")
# Accessing Class varibles
print(Lata.categoty)
# Accessing Class Methods
Lata.hello()

# Using 'self' to access class variables
class TingaBapa:
    category = "smoking"
    # Using 'self' to access class members
    def bapaSmokes(self):
        print(f"Tinga Bapa {self.category}")
        
# TingaBapa.bapaSmokes() # Gives error like one positional arguments reuired
# Giving context class name TingaBapa' to 'bapaSmokes'
TingaBapa.bapaSmokes(TingaBapa) # Tinga Bapa smoking
bapa = TingaBapa()
TingaBapa.bapaSmokes(bapa)