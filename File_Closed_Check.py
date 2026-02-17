# Python File I/O: Assess if a file is closed or not

# Write a Python program to assess if a file is closed or not.

def check_file_status(file_path):
    # Initializing the file variable
    
    f = open(file_path, 'w')
    
    print(f'1. Is the file closed immediately after open()? {f.closed}')
    
    try:
        f.write('Checking file status....')
    finally:
        f.close()
        print(f'2. Is the file closed after calling .close()? {f.closed}')
        
    
    print('-' * 55)

    # Demonstrating with a context maneger (the "Pythonic way")
    with open(file_path,'r') as f_auto:
        print(f"3. Inside 'with' block, is file closed? {f_auto.closed}")
        
    print(f"4. Outside 'with' block, is file closed? {f_auto.closed}") 

# Usage

check_file_status('first.txt')