from pathlib import Path

# ------------------------------ Listing every file in a directory

# p1 = Path(r"S:\Elektronik\E2\E2V1\E2V1P\E2V1P_Products\NEDAP\07_AV\02_BoxBuild\02_PxN")
p1 = Path(r"D:\Szakdoga_copy")
files = [p for p in p1.rglob("*") if p.is_file()]

# ------------------------------ Grouping files by extensions

grouped_files = {}

for file in files:
    if file.suffix in grouped_files:
        grouped_files[file.suffix].append(file.stem)
    else:
        grouped_files[file.suffix] = [file.stem]

# ------------------------------ Creating a folder for each extension (commented out, only need it once)

# for key in grouped_files:
#     new_dir = p1 / f"{key}"
#     new_dir.mkdir(parents=True, exist_ok=True)
#

# ------------------------------ Moving files with different extensions into their respective folder

for file in files:
    file.move_into(Path(f"{p1 / file.suffix}"))

