from libs.greeting.lib import greet, farewell, formal_greet, casual_greet

def hello():
    """Print greeting message."""
    print("Hello, World!")

def main():
    print(greet("Alice"))
    print(formal_greet("Smith", "Dr."))
    print(casual_greet("Bob"))
    print(farewell("Everyone"))

if __name__ == "__main__":
    main()
