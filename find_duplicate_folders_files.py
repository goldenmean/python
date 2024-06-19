'''
List all folders and files in the provided directory and 
create a text file of duplicate files and folders with their full path

'''


import os
import collections
import sys




def find_duplicates(directory):
    """
    Find duplicate files and folders in the provided directory and its sub-directories,
    and create a text file with their names and full paths.
    """
    # List all files and folders in the directory and its sub-directories
    entries = []
    for root, dirs, files in os.walk(directory):
        #print(root, dirs, files)
        for file in files:
            entries.append(os.path.join(root, file))
        for subdir in dirs:
            entries.append(os.path.join(root, subdir))

    #print(f"entries: {entries}")
    # Group entries by their name
    groups = collections.defaultdict(list)
    for entry in entries:
        groups[os.path.basename(entry)].append(entry)
	
    print(groups)
    #print(f"groups keys: {groups.keys()}")
    #print(f"groups values: {groups.values()}")

    # Create a text file with duplicate names and full paths
    with open('duplicate_names.txt', 'w') as f:
        for name, paths in groups.items():
            if len(paths) > 1:
                f.write('Duplicate: {}\n'.format(name))
                for path in paths:
                    f.write('    {}\n'.format(path))

    print('Done!')



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python find_duplicate_folders_files.py <directory>')
    else:
        directory = sys.argv[1]
        print(directory)
        find_duplicates(directory)


    
