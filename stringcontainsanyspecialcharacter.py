# Program to check if a string contains any special character


n = "Geeks$For$Geeks"

# c = 0

# s = '[@_!#$%^&*()<>?/:]'

# for i in n:
    # if i in s:
        # c +=1
        
        
# if c:
    # print('string is not excepted')
# else:
    # print('string excepted')
# ===========================


def check_special_char_ascii(str1):
    for char in str1:
        if ord(char) < 48 or (57 < ord(char) < 65) or (90 < ord(char) < 97) or ord(char) > 122:
            return "String is not accepted."
    return "String is accepted."


str1 = "Geeks$For$Geeks"
print(check_special_char_ascii(str1))