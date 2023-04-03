class Marvel:

def __init__(self, name, health, attackPower, armorumber):
self.name = name
self.health = health
self.attackPower = attackPower
self.armorNumber = armorhumber

def serang(self, lawan):
print(self.name + " menyerang " + lawan.name)
lawan.diserang(self, self.attackPower)

def diserang(self, lawan, attackPower_lawan):
print(self.name + " diserang " + lawan.name)
attact_diterima = attackPower_lawan
print(“Serangan terasa : " + str(attact_diterima))
self.health -= attact_diterima

print(“"Darah " + self.name + " tersisa " + str(self.health))

ironman = Marvel(“Iron Man",100,18,5)
thor = Marvel(“Thor",95,15,18)

#ironman. serang()
ironman.serang (thor)
#print("\n")
#ironman. serang(thor)
#print("\n")
#thor.serang(ironman)
