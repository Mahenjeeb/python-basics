# MRO - Method Resolution Order
class Lata:
    does = "Kanduri"
class DantaRagudi(Lata):
    does = "Kata Kata"
class Tinga(Lata):
    does = "Tingisa"
class Bapa(DantaRagudi, Tinga):
    pass
    
behaves = Bapa()
# "Kata Kata" BEcause of MRO it takes DantaRagudi 
# class first then Tinga
print(behaves.does) # "Kata Kata"

# To see MRO order use '__mro__' with class name
print(Bapa.__mro__)