# Python File I/O: Get the file size of a plain file

# Write a Python program to get the file size of a plain file.

import os

file_path = 'notes.txt'

if os.path.exists(file_path):
    
    file_size = os.path.getsize(file_path)
    print(f'File size: {file_size} bytes')

else:
    print('File does not exist.')

