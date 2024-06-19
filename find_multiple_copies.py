

import os
import hashlib
import collections

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
            with open(file_path, 'rb') as f:
                file_content = f.read()
                file_hash = hashlib.md5(file_content).hexdigest()
                file_hashes[file_hash].append(file_path)

    # Filter out unique files (only keep duplicates)
    duplicate_files = {hash: paths for hash, paths in file_hashes.items() if len(paths) > 1}

    # Create a text file with duplicate files and their full paths
    with open('duplicate_files.txt', 'w') as f:
        for hash, paths in duplicate_files.items():
            f.write('Duplicate Hash: {}\n'.format(hash))
            for path in paths:
                f.write('    {}\n'.format(path))

    print('Done!')

# Example usage
find_duplicate_files_with_same_content('/path/to/directory')