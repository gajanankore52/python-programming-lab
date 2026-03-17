# Write a Python program to create a person class. Include attributes like name, country and date of birth. 
# Implement a method to determine the person's age

from datetime import date

class Person:
    def __init__(self, name, country, birth_date):
        """
        Initialize the person.
        :param name: str
        :param country: str
        :param birth_date: date object (year, month, day)
        """
        self.name = name
        self.country = country
        self.birth_date = birth_date
        
    
    def calculate_age(self):
        """Calculate the person's age based on the current date."""
        today = date.today()
        # Initial age calculation based on years
        age = today.year - self.birth_date.year
        
        # Check if the birthday has occured yet this year
        # (today.month, today.day) < (birth_date.month, birth_date.day) returns (1) or False (0)
        has_had_birthday_this_year = (today.month, today.day) >= (self.birth_date.month, self.birth_date.day)
        
        if not has_had_birthday_this_year:
            age -=1
        
        return age      

        
# Example Usage
# Create a date object: date(Year, Month, Day)
person1 = Person("Alex", "Canada", date(1997, 5 , 21))

print(f"Name: {person1.name}")
print(f"Country: {person1.country}")
print(f"Age: {person1.calculate_age()}")
