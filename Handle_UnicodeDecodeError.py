# Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.
# Raised when a Unicode-related error occurs during decoding. It is a subclass of UnicodeError.

def read_file_safely(filename, encoding_type='utf-8'):
    try:
        print(f"Attempting to read '{filename}' using {encoding_type}...")
        with open(filename, 'r', encoding=encoding_type) as file:
            data = file.read()
            print("File read successfully!")
            return data

    except UnicodeDecodeError as e:
        print(f"Encoding Error: The file is not in {encoding_type} format.")
        print(f"Details: {e}")
        # Fallback strategy: Suggesting an alternative encoding
        print("Tip: Try opening the file with 'latin-1' or 'utf-16'.")
        
    except FileNotFoundError:
        print("Error: File not found.")


# Testing the function
# (In a real scenario, this would trigger if 'unicode.txt' contained non-UTF8 binary data)
read_file_safely("unicode.txt", encoding_type='utf-8')