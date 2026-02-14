# Python File I/O: Read a file line by line store it into a variable

# Write a Python program to read a file line by line store it into a variable.


def file_to_variable(file_path):
    
    try:
        
        with open(file_path, 'r', encoding = 'utf-8') as file:
            #This variable now holds every line as a separate string in a list
            
            content_list = [line.rstrip() for line in file]
        
        return content_list
    
    except FileNotFoundError:
        return "Error: File not found."
        

#Usage

if __name__ =="__main__":
    
    file_data = file_to_variable('notes.txt')
    
    # Now you can access any line by its index
    
    if isinstance(file_data,list):
        
        print(f'The first line is: {file_data[0]}')
        print(f'Total lines stored: {len(file_data)}')
        
    