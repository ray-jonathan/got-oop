# These aren't "real" or robust tests.

from character import Character

# Characters can be instantiated with name and avatar
arya = Character("Arya Stark", "arya.png")
jon = Character("Jon Snow", "jon.jpg")

print(arya.name, arya.avatar)
print(jon.name, jon.avatar)