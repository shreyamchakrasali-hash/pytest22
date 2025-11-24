import sys

def add(a, b):
    return a + b

if name == "main":
    # Ensure correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: python add.py <num1> <num2>")
        sys.exit(1)

    # Convert arguments to integers
    x = int(sys.argv[1])
    y = int(sys.argv[2])

    # Print the sum
    print("Sum:", add(x, y))
