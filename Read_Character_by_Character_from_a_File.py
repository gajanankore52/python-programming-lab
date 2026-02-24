# Python Program to Read Character by Character from a File


def read_char_by_char(file_path):
    try:
        with open(file_path, 'r',encoding='utf-8')as file:
            
            while True:
                # Read exactly one character
                char = file.read(1)
                
                if not char:
                    break
                
                print(char)
                
    except FileNotFoundError:
        print('f')

# Usage
read_char_by_char('original.txt')