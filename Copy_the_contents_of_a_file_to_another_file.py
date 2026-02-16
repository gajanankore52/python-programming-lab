# Python File I/O: Copy the contents of a file to another file

# Write a Python program to copy the contents of a file to another file .

# Using shutil module

# import shutil

source = "original.txt"
destination = "backup.txt"

# try:
    
    # shutil.copyfile(source, destination)
    # print(f'Successfully copied {source} to {destination}')
    
# except FileNotFoundError:
    
    # print('Error: The source file does not exist.')

# except PermissionError:
    
    # print("Error: Permission denied.")

# =================================

with open(source, 'rb') as src,open(destination, 'wb') as dst:
    dst.write(src.read())
