from pathlib import Path

p1 = Path(r"C:\Users\bblas\OneDrive\Pictures")
files = list(p1.iterdir())

for file in files:
    print(file)

# Listing every file in a directory