# Write a Python program to append text to a file and display the text.

def append_and_display(file_path, new_content):

    # Strip whitespace to ensure we aren't adding empty lines
    new_content = new_content.strip()

    if not new_content:
        print("No content provide to append.")
        return
    
    try:
        # 'a+' opens for appending and reading
        with open(file_path, 'a+', encoding='utf-8') as file:
            # write the text
            file.write(new_content + '\n')
            
            # Move the 'cursor' back to the begining to read everything
            file.seek(0)

            print(f'--- Updated Content of {file_path} ---')
            print(file.read())
            print("-" * 30)    
    
    except PermissionError:
        print(f"Error: You don't have permission to edit '{file_path}'.")
    
    except Exception as e:
        print(f'An unexpected error occured: {e}')

if __name__ == "__main__":
    
    filename = "notes.txt"
    text_to_add = " This is new line added to the end."
    
    append_and_display(filename, text_to_add)