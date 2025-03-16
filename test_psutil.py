


import psutil
import os

print(f"Process ID: {os.getpid()}")
print(f"CPU Usage: {psutil.cpu_percent()}%")
print(f"Memory Usage: {psutil.Process().memory_info().rss / 1024 / 1024} MB")

