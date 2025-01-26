



def test_file_readline():
    with open('sample.txt', 'r') as f:
        for _ in range(10):
            line = f.readline()
            if not line:
                break
            print(line.strip())

def test_file_read_next():
    with open('sample.txt', 'r') as f:
        for _ in range(10):
            line = next(f, None)
            if not line:
                break
            print(line.strip())
    
print(f"Reading file using next( ) function")
test_file_read_next()

print(f"Reading file using readline( ) function")
test_file_readline()