# Python program to read file word by word


def read_word_by_word(file_path):
    try:
        with open(file_path,'r',encoding='utf-8') as file:
            for line in file:
                # .split() handles spaces,tabs, and newlines
                words = line.split()
                for word in words:
                    print(word)
    except FileNotFoundError:
        print('File not found.')
       
       
# Usage
read_word_by_word('original.txt')