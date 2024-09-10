'''
We are given  a string:  
"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"  
which represent a directory structure as below:
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

Parse the string to get the directory structure 
'''


def parse_directory_structure(s):
    lines = s.split('\n')
    structure = {}
    path = []

    for line in lines:
        depth = line.count('\t')
        name = line.strip()

        while len(path) > depth:
            path.pop()

        if depth == len(path):
            path.append(name)

        current = structure
        for dir in path[:-1]:
            if dir not in current:
                current[dir] = {}
            current = current[dir]

        if '.' in name:  # It's a file
            current[name] = None
        else:  # It's a directory
            if name not in current:
                current[name] = {}

    return structure

# Test the function
s = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
result = parse_directory_structure(s)
print(result)