

import os
import hashlib
import collections
import sys

def find_duplicate_files_with_same_content(directory):
    """
    Find duplicate files with the same content but different names in the provided directory and its sub-directories,
    and create a text file with their names and full paths.
    """
    # Dictionary to store file hashes
    file_hashes = collections.defaultdict(list)

    # Traverse all files in the directory and its sub-directories
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)			
            with open(file_path, 'rb') as f:
                file_content = f.read()
                file_hash = hashlib.md5(file_content).hexdigest()
                file_hashes[file_hash].append(file_path)
	
    # Filter out unique files (only keep duplicates)
    duplicate_files = {hash: paths for hash, paths in file_hashes.items() if len(paths) > 1}

    # Create a text file with duplicate files and their full paths
    with open('copies_of_files.txt', 'w') as f:
        for hash, paths in duplicate_files.items():
            f.write('Duplicate Hash: {}\n'.format(hash))
            for path in paths:
                f.write('    {}\n'.format(path))

    print('Done!')

# Example usage
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python find_multiple_copies.py <directory>')
    else:
        directory = sys.argv[1]
        #print(directory)
        find_duplicate_files_with_same_content(directory)
		
		