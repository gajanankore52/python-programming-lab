# File operation: Read First N Lines


def read_first_n_lines(file_path,n):
   
    try:
        with open(file_path,'r',encoding='utf-8') as file:
            ## We use a loop to avoid loading the entire file into memory
            
            for i in range(n):
                line = file.readline()
               
                if not line:
                    print('Hello')
                    break # Stop if we reach the end of the file early
                
                print(line.strip())
              
    except FileNotFoundError:
        print(f'Error: The file at {file_path} was not found.')
    
    except Exception as e:
        print(f'An unexpected error occured: {e}')

if __name__=="__main__":
    filename = 'example.txt'
    lines_to_read = 5
    read_first_n_lines(filename,lines_to_read)