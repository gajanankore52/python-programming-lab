
# Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
# exception FileNotFoundError:
# Raised when a file or directory is requested but doesn’t exist. Corresponds to errno ENOENT.

def read_user_file(filename):
    try:
        # Attempt to open and read the file
        with open(filename, 'r')as file:
            content = file.read()
            print("File content successfully loaded:")
            print(content)
            
    except FileNotFoundError:
        # Specifically handle the case where the file is missing
        print(f'Error: The file "{filename}" was not found.')
        print("Please check the file path and try again.")
        
    except PermissionError:
        # Handle cases where the file exists but you can't open it
        print(f'Error: Youdo not have permission to read "{filename}".')
        

# Testing with a non-existent file
read_user_file("my_secret_notes.txt")