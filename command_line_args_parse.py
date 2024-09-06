'''
Parsing commandline arguments in python
'''


'''
## Using builtin sys module
import sys

# Access the command-line arguments
args = sys.argv
#args is a list of command-line arguments passed to the script

# The first argument is always the script name, so we skip it
script_name = args[0]
input_file = args[1] if len(args) > 1 else None
output_file = args[2] if len(args) > 2 else None
verbose = '--verbose' in args or '-v' in args

if not input_file or not output_file:
    print(f"Usage: {script_name} <input_file> <output_file> [--verbose|-v]")
    sys.exit(1)

if verbose:
    print(f'Input file: {input_file}')
    print(f'Output file: {output_file}')
    print('Verbose mode is enabled')

# Your code logic here
print(f'Processing {input_file} and saving results to {output_file}')

#Use the script with below commandline arguments
# python script.py input.txt output.txt --verbose

'''

## Using argparse module
import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Example of command-line argument parsing.')

# Add arguments
parser.add_argument('input', type=str, help='Input file name')
parser.add_argument('output', type=str, help='Output file name')
parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose mode')

# Parse the arguments
args = parser.parse_args()
print("Using argparse module")
print(args)
print(type(args.verbose))

# Access the arguments
input_file = args.input
output_file = args.output
verbose = args.verbose

if verbose:
    print(f'Input file: {input_file}')
    print(f'Output file: {output_file}')
    print('Verbose mode is enabled')

# Your code logic here
print(f'Processing {input_file} and saving results to {output_file}')