# Python program to capitalize the first and last character of each word in a string

def capitalize_edges(text):
    words = text.split()
    
    # Logic: If word length > 1, capitalize both ends. 
    # Otherwise, just capitalize the single letter.
    res = [
        word[0].upper() + word[1:-1] + word[-1].upper() if len(word) > 1 
        else word.upper() 
        for word in words
    ]
    
    return ' '.join(res)


def main():
    s1 = "a"
    s2 = "welcome to a python world" # Added 'a' to test single-character logic
    
    print(f"Original: {s1} -> Result: {capitalize_edges(s1)}")
    print(f"Original: {s2} -> Result: {capitalize_edges(s2)}")

if __name__ == "__main__":
    main()