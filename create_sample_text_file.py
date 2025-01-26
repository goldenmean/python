

def create_test_file():
    with open("sample.txt", "w") as f:
        for i in range(50):
            f.write(f"This is line {i+1}\n")

create_test_file()
