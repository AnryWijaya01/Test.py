class Marvel:

def __init_(self, inputName, inputHealth, inputPower, inputArmor):
# instance variable

self.name = inputName
self.health = inputtealth
self.power = inputPower
self.armor = inputArmor

# void function, method tanpa return
def siapa(self):
print("Namaku adalah :

+ self.name)

# method dengan argumen
def healthTambah(self, tambah):
self.health += tambah

# method dengan return
def getHealth(self):
return self.health

marvell = Marvel("Iron Man",1000,900,800)
marvel2 = Marvel("Thor",900,1000,900)
marvel3 = Marvel("Iron Man",800,700,600)

# pemanggilan method
marvell.siapa()

# pemakaian method dengan argumen
marvell.healthTambah(10)
print (marvell.health)

# mengembalikan nilai dengan method
print (marvell.getHealth())
