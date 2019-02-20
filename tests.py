# These aren't "real" or robust tests.

from character import Character

# Characters can be instantiated with name and avatar
arya = Character("Arya Stark", "arya.png")
jon = Character("Jon Snow", "jon.jpg")

print(arya.name, arya.avatar)
print(jon.name, jon.avatar)

# after adding 2 items to inventory, length of inventory should equal 2

arya.inventory.append("sword")
arya.inventory.append("mask")
jon.inventory.append("dragon glass")


print(len(arya.inventory))
print(len(jon.inventory))