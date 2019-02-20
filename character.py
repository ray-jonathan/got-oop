# name
# avatar
# inventory

# class names a single words, with the first letter capitalized
class Character():
    # the "dunder init" method is the constructor
    def __init__(self, new_name, new_avatar):
        # `self` is the customary way to refer to the instance being built
        # in some other languages, they use `this` instead
        self.name = new_name
        self.avatar = new_avatar
        self.inventory = []

    # `someone=None` is a default argument
    # `None` is equivalent to `null` in other languages
    def greet(self, someone=None):
        # When we assume that `someone` argument has a `.name` property,
        # this is an Object-Oriented Programming principle called polymorphism
        # In Python, it's called "Duck Typing" ("... if walks like a duck, talks like a duck...")
        if someone is not None:
            return "Hello, %s, I am %s. You killed my father. Prepare to die." % (someone.name,self.name)
        else:
            return "Hello, I am %s. You killed my father. Prepare to die." % (self.name,)

# Hero is a kind of Character
# Hero is a subclass of Character
# Hero inherits from character
# Character is the super class of Hero (aka parent)


class Hero(Character):
    def attack(self, someone=None):
        if someone is not None:
            return "Who do you think you are, %s?! You're going to regret tangling with me!" % (someone.name,)
        else:
            return "Who do you think you are?! You're going to regret tangling with me!"

class Monster(Character):
    def groan(self, someone=None):
        if someone is not None:
            return "Grrgrg, %s, I am %s. I pose a threat to you grgrgrgr." % (someone.name,self.name)
        else:
            return "Grrgrg, I am %s. I pose a threat to you grgrgrgr." % (self.name,)