# File Operation: Append Text and Display

# Write a Python program to append text to a file and display the text.

def append_and_display(file_path, new_content):
    
    try:
        
        with open(file_path,'a',encoding='utf-8') as file:
            file.write(new_content + '\n')
            
        print(f"Successfully added: {new_content}")
        
        print("-"*20)
        
        with open(file_path, 'r' , encoding='utf-8') as file:
            
            print("Current File Content:")
            print(file.read())
    
    except Exception as e:
        print(f'An error occured: {e}')

if __name__ == "__main__":
    
    filename = "notes.txt"
    text_to_add = " This is new line added to the end."
    
    append_and_display(filename, text_to_add)