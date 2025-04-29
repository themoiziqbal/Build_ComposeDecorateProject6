# Constructors and destructors

# A class Logger that logs when an object is created, and when it is destroyed

class Logger:
    def __init__(self):
        print(f"Logger instance #{id(self)} created")

    def __del__(self):
        print(f"Logger instance #{id(self)} destroyed")

def create_logger():
    _ = Logger()
    print("End of create_logger function")

def main():
    # Create three instances
    objects : list[Logger] = []

    for _ in range(0,3):
        objects.append(Logger())
    
    # Call one instance inside a function
    create_logger()
    
    # Let's see how it all ends
    print("End of main function")

if __name__ == '__main__':
    _ = Logger()
    main()
    print("End of check that runs main")