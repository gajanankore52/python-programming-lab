# Python File I/O: Read last n lines of a file
# Write a Python program to read last n lines of a file.


def read_last_n_lines(file_path,n):
    
    try:
        
        with open(file_path,'r',encoding='utf-8') as file:
            #Read all lines into a list
            lines = file.readlines()
            
            # Use slicing to get the lst n elements
            
            last_lines = lines[-n:]
            
            for line in last_lines:
                print(line.strip())
                
    except FileNotFoundError:
        print('File not found.')

# Usage
if __name__ =="__main__":
    read_last_n_lines('notes.txt',2)

