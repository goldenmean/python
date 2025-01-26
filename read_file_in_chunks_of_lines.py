def read_lines_in_chunks(filename, chunk_size=5):
    with open(filename, 'r') as file:
        while True:
            # Read chunk_size lines at a time
            lines = [next(file, None) for _ in range(chunk_size)]
            
            # Remove None values (end of file)
            lines = [line for line in lines if line is not None]
            
            # If no lines were read, exit loop
            if not lines:
                break
            
            print(lines)
            # Process the chunk of lines
            yield lines
            

def read_with_return(filename, chunk_size=3):
    with open(filename, 'r') as file:
        
        lines = [file.readline().strip() for _ in range(chunk_size)]
        # for _ in range(chunk_size):
        #     line = file.readline()
        #     if line:  # Check if line is not empty
        #         #lines.append(line.strip())
        #         lines.append(line)
        print(lines)
        return lines

# Example usage
if __name__ == "__main__":
    # Sample usage of the function
    no_of_lines = 7
    for chunk in read_lines_in_chunks("sample.txt", no_of_lines):
    #for chunk in read_with_return("sample.txt", no_of_lines):
        print(len(chunk))
        print(f"Processing chunk of {no_of_lines} lines:")
        for line in chunk:
            print(line.strip())
        print("-" * 20)