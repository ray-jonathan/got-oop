# These aren't "real" or robust tests.

from character import Character
from character import Hero
from character import Monster

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

# arya should hava a `greet` method
# and when I call it with `arya.greet()`, it should return 
# "Hello,I am Arya Stark. You killed my father. Prepare to die."
print(arya.greet())

# arya should hava a `greet` method
# and when I call it with `arya.greet(jon)`, it should return 
# "Hello, Jon Snow, I am Arya Stark. You killed my father. Prepare to die."
print(arya.greet(jon))

# I should be able to create a Hero instance
bronn = Hero("Bronn of the Blackwater", "bron.gif")
mittens = Monster("Mittens the Kitten", "mitten.jpeg")

# Hero should be able to `.greet` Character
print(bronn.greet(arya))
print(jon.greet(bronn))

# Monster should be able to `.groan` a Character or Hero
print(mittens.groan(arya))
print(mittens.groan(bronn))
print(bronn.attack(mittens))