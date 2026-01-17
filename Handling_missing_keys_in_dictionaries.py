# Handling missing keys in Python dictionaries

# Python Program to Handling Missing keys in Dictionaries Using get()

# country_code = {'India' : '0091',
                # 'Australia' : '0025',
                # 'Nepal' : '00977'}
                
# print(country_code.get('India'))

# print(country_code.get('U.S.A.','Not Found'))
# ======================================================================


# Handling Missing keys in Python Dictionaries Using setdefault()

country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}
                

country_code.setdefault('Japan','Not Present')

print(country_code['India'])

print(country_code['Japan'])