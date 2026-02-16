# Python File I/O: Write a List content to a file

# Write a Python program to write a list content to a file.


fruits = ["Apple", "Banana", "Cherry", "Date"]

# 'w' opens the file for writing (overwrites existing content)
# with open('list_output.txt','w') as file:
    # for item in fruits:
        # file.write(f'{item}\n')

# print('File written successfully!')

# ===========================================

with open('list_output.txt','w') as file:
    # Adding \n to each item using a list comprehension
    
    file.writelines(f'{item}\n' for item in fruits)

print('File written successfully!')
