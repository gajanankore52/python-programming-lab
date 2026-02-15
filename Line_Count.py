# Line Count

# Write a Python program to count the number of lines in a text file.


def count_lines_efficient(file_path):
    
    try:
        count = 0
        
        with open(file_path, 'r' ,encoding = 'utf-8')as file:
            
            for line in file:
                count += 1
        return count
        
    except FileNotFoundError:
        return 'Error: File not found.'

#Usage
if __name__ =="__main__":
    
    filename = 'notes.txt'
    print(f'Total lines: {count_lines_efficient(filename)}')