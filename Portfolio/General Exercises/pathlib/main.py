from pathlib import Path

# Listing every file in a directory

p1 = Path(r"S:\Elektronik\E2\E2V1\E2V1P\E2V1P_Products\NEDAP\07_AV\02_BoxBuild\02_PxN")
files = [p for p in p1.rglob("*") if p.is_file()]

# grouping files by extensions

grouped_files = {}

for file in files:
    grouped_files[file.suffix] = file.stem

print(grouped_files)
