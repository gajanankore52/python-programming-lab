# Python File I/O: Read a file line by line and store it into a list

# Write a Python program to read a file line by line and store it into a list.

def file_to_list_clean(file_path):
    
    try:
        with open(file_path,'r', encoding='utf-8') as file:
            # .strip() remove the newline character fro each line
            
            lines_list = [line.strip() for line in file]
            
        return lines_list
    
    except FileNotFoundError:
        return "File not found."



# Usage
if __name__ =="__main__":
    my_list = file_to_list_clean('notes.txt')
    print(my_list)
