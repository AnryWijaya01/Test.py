class Marvel:
def __init__(self, inputName, inputHealth, inputPower, inputArmor):
self.name = inputName
self.health = inputHealth
self.power = inputPower
self.armor = inputArmor

marvell = Marvel("Iron Man",166,16,90)
marvel2 = Marvel("Thor",90,15,108)
marvel3 = Marvel(“Captain America",86,5,78)

print(marvel1.name)
print(marvel2.health)
print(marvel3.__dict__)

