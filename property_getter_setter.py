



#Python @property getter method
class Example:
    @property
    def value(self):
        return "This is a getter method."
    
e = Example()
print(e.value)  # Accesses the getter method like an attribute

print("-------------------------------------------")


# getter and setter method
class Example2:
    #getter 
    @property
    def value(self):
        print("Executing the getter")
        return self._internal_value

    #setter
    @value.setter
    def value(self, new_value):
        print("Executing the setter")
        self._internal_value = new_value

e = Example2()
e.value = "Setting New Value"  # Uses the setter method to modify the attribute
print(e.value)  # Accesses the getter method

print("-------------------------------------------")

# Deleter example
class Example3:
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._value = new_value

    @value.deleter
    def value(self):
        print("Executing the deleter")
        del self._value
    

e = Example3()  # Creates an instance of the class
e.value = "Setting value to call deleter later"
print(e.value)  # Accesses the getter method
del e.value  # Uses the deleter method to delete the attribute
#print(e.value)  #Accessing the attribute after deleter being called gives AttributeError exception

