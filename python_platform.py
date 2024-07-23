import platform

print(platform.python_version())
print(platform.python_revision())
#print(platform.python_version_tuple())
print(platform.python_compiler()) 
print(platform.python_implementation()) #CPython or IronPython
print(platform.python_build())
print(platform._sys_version()) #Full details of Python implementation, version, revision, build
print(platform.machine()) # 64 bit or 32 bit
print(platform.uname()) # OS details  e.g. system=Windows release=11 machine=AMD64


