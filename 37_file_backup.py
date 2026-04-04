
# Write a Python program to copy the contents of a file to another file .


import shutil
import os

source = "original.txt"
destination = "backup.txt"

source = "original.txt"
destination = "backup.txt"

# 1. Professional Method (shutil.copy2 preserves metadata like timestamps)
def professional_copy(src,dst):
    try:
    
        shutil.copy2(src, dst)
        print(f'Successfully backed up {src}')
    
    except IOError as e:
    
        print(f'Unable to copy file. {e}')

# 2. Manual Method (Chunk-based for memory efficiency)
def manual_copy(src,dst):
    try:
        count =0
        with open(src,'rb') as fsrc:
            print("1")
            with open(dst,'wb') as fdst:
                print("2")
                # Read 1 MB at a time
                while True:
                    buf = fsrc.read(1024 * 1024)
                    if not buf:
                        break
                    fdst.write(buf)

    except FileNotFoundError:
        print('Source file not found.')
manual_copy(source,destination)
