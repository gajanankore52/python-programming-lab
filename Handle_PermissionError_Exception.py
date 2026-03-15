# Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue
# Raised when trying to run an operation without the adequate access rights - for example filesystem permissions. Corresponds to errno EACCES, EPERM, and ENOTCAPABLE.

import os

def write_to_protected_file(filename):
    try:
        print(f"Atempting to open '{filename}' for writing...")
        
        # 'w' mode requires write permissions from the os
        with open(filename, 'w') as file:
            file.write("Attempting to save data.")
            print("Success: File written successfullt.")
            
    except PermissionError as e:
        # Trigged by EACCES, EPERM, OR ENOTCAPABLE
        print(f"Permission Denied: You do not have the required access rights.")
        print(f"System Error Details: {e}")
        
    except Exception as e:
        # Catch-all for other unexpected issues
        print(f"An unexpected error occured: {e}")
        

# Example Usage

write_to_protected_file("backup.txt")






