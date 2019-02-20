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
        if someone is not None:
            return "Hello, %s, I am %s. You killed my father. Prepare to die." % (someone.name,self.name)
        else:
            return "Hello, I am %s. You killed my father. Prepare to die." % (self.name,)