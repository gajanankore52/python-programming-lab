# File Operations: Read Entire File


def read_entire_file(file_path):
    
    try:
        with open(file_path,'r',encoding='utf-8') as file:
            
            content = file.read()
            print(content)
           
            
    
    except FileNotFoundError:
        print("Keep calm, but that file doesn't exist")


read_entire_file('example.txt')