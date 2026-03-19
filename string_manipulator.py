# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.


class StringProcessor:
    
    def __init__(self):
        self.user_string = ""
        
    
    def getString(self):
        """Gets a string from console input."""
        self.user_string = input("Please enter a string: ")
        
    def printString(self):
        """prints the string in upper case."""
        print(self.user_string.upper())

def test_string_processor():
    """Simple test function to verify the class methods."""
    
    processor = StringProcessor()
    processor.getString()
    processor.printString()

# This ensures the test only runs if the script is executed directly
if __name__ == "__main__":
    test_string_processor()