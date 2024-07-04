'''
Simplifying absolute paths
Consider a absolute path which can have "." , ".." , "/", or multiple "///"
"." represents the current directory
".." represents the parent directory
"/" represents the root directory
"//" or multiple "/" can be neglected and treated as single "/"
Given a absolute path find the simplified path 
e.g. 
1] Input = "/a/./b/../c"
   output = "/a/c" 

2] Input = "/a/../../b/../c//.//"
   output = "/c"

3] Input = "/a//b////c/d//././/.."
   output = "/a/b/c"

4] Input = "/a/./b/../../c"
   Output= "/c"
 
'''

def simplify_path(path):
    # Split the path by "/" and initialize a stack
    parts = path.split("/")
    stack = []
    
    for part in parts:        
        if part == "..":
            #if part is .. pop from stack indicating we traverse to root folder
            if stack:
                stack.pop()
        elif part and part != ".":
            # Ignore empty or "." parts and add the non-empty path part to stack
            stack.append(part)
    
    # Join the components in the stack
    simplified_path = "/" + "/".join(stack)
    
    return simplified_path

# Test cases
print(simplify_path("/a/./b/../c"))  # Output: "/a/c"
print(simplify_path("/a/../../b/../c//.//"))  # Output: "/c"
print(simplify_path("/a//b////c/d//././/.."))  # Output: "/a/b/c"
print(simplify_path("/a/./b/../../c"))
    

