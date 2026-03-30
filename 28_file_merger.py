# Write a Python program to combine each line from first file with the corresponding line in second file.

def combine_files(file1_path, file2_path):
    
    try:
        
        with open(file1_path, 'r', encoding='utf-8') as f1,\
             open(file2_path, 'r', encoding='utf-8')as f2:
        
            # Zip pairs line 1 of f1 with line 1 of f2, and so on 
            for line1,line2 in zip(f1,f2):
                # .strip() removes existing newlines so we can control the output
                combined = f'{line1.strip()} {line2.strip()}'
                
                print(combined)
    
    except FileNotFoundError:
        
        print('Error: One or both files wre not found.')
    
    except Exception as e:
        
        print(f'An error occured: {e}')
                


# Usage

combine_files('first.txt','second.txt')