# Given a text file containing several key-value pairs in the format key = value, find how many times a specific key-value pair occurs in the file.



def count_kv_pair(file_path, search_key, search_value):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Skip empty lines
                if not line.strip():
                    continue
                
                # Split line into key and value at the first '='
                if '=' in line:
                    key, value = line.split('=', 1)
                    
                    # .strip() removes leading/trailing spaces and newlines
                    if key.strip() == search_key and value.strip() == search_value:
                        count += 1
                        
        return count

    except FileNotFoundError:
        print("Error: The file was not found.")
        return 0

# Execution
target_key = "name"
target_value = "Jennie"
filename = "fruits.txt"

occurrences = count_kv_pair(filename, target_key, target_value)
print(f"Occurrences of '{target_key}={target_value}' : {occurrences}")