# Python @dataclass examples
# automatically generates several special methods, such as init(), repr(), and eq()

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    height: float

"""

#1] When creating simple data containers
@dataclass
class Point:
    x: float
    y: float

p1 = Point(1.0, 2.0)
p2 = Point(3.0, 4.0)    

print(p1)  # Output: Point(x=1.0, y=2.0)
print(p2)  # Output: Point(x=3.0, y=4.0)


 #2] When automatic string representation is needed   
@dataclass
class Book:
    title: str
    author: str
    year: int

book = Book("1984", "George Orwell", 1949)
print(book)  # Output: Book(title='1984', author='George Orwell', year=1949)

#3] For easy comparion between class objects
@dataclass
class Employee:
    name: str
    id: int

e1 = Employee("Alice", 12345)
e2 = Employee("Alice", 12345)
print(e1 == e2)  # Output: True

""" 
#4] For easy creation of dictionaries
@dataclass  
class Config:       
    name: str           
    value: str              
    description: str = None 

config = Config("key1", "value1")
print(config)  # Output: Config(name='key1', value='value1', description=None)  
print(config.__dict__)  # Output: {'name': 'key1', 'value': 'value1', 'description': None}  

#5] When we want to create immutable objects
@dataclass(frozen=True)
class Configuration:
    host: str
    port: int

config = Configuration("localhost", 8080)
print(config)  # Output: Configuration(host='localhost', port=8080)     
#config.port = 9090  # This will raise a dataclasses.FrozenInstanceError

#6] Default values and post-init processing 
from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 3
    total_value: float = field(init=False)

    def __post_init__(self):
        self.total_value = self.price * self.quantity

product = Product("iPhone", 1000.0)
print(product)  # Output: Product(name='iPhone', price=1000.0, quantity=0, total_value=0.0)
print(product.__dict__)  # Output: {'name': 'iPhone', 'price': 1000.0, 'quantity': 0, 'total_value': 0.0}   

