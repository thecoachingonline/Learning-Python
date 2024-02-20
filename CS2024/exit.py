import sys

if len(sys.argv) != 2:
    print("Missing argument")
    sys.exit()

print(f"Hello, {sys.argv[1]}")
sys.exit(0)