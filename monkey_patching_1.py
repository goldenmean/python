class Cat:
    def meow(self):
        return "Meowww!"

# Monkey patch to extend functionality
def ragdoll_meow(self):
	return "Ragdoll cat Miaowww!"

original_meow = Cat.meow
Cat.meow = ragdoll_meow

ragdoll = Cat()
print(ragdoll.meow())  # Output: Ragdoll cat Miaowww!

# Undo monkey patch
Cat.meow = original_meow   
print(ragdoll.meow())  # Output: Meowww!

