
# Singleton design pattern class 
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Usage
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # True

# Thread safe Singleton class
import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(ThreadSafeSingleton, cls).__new__(cls)
        return cls._instance

# Usage
singleton1 = ThreadSafeSingleton()
singleton2 = ThreadSafeSingleton()

print(singleton1 is singleton2)  # True