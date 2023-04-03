class Marvel:
# class variable
jumlah =

def __init__ (self, inputName, inputHealth, inputPower, inputArmor):
# instance variable
self.name = inputName
self.health = inputHealth
self.power = inputPower
self.armor = inputArmor
Marvel.jumlah += 1
print(“Hero Marvel dengan nama : " + inputName)

marvell = Marvel("Iron Man",1008,900,3080)
print(Marvel.jumlah)

marvel2 = Marvel("Thor",208,1008,900)
print(Marvel.jumlah)

marvel3 = Marvel("Captain America",800,700,600)
print(Marvel.jumlah))]
