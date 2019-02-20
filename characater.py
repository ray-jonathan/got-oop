# name
# avatar
# inventory

# class names a single words, with the first letter capitalized
class Character():
    # the "dunder init" method is the constructor
    def __init__(self, new_name):
        # `self` is the customary way to refer to the instance being built
        # in some other languages, they use `this` instead
        self.name = new_name