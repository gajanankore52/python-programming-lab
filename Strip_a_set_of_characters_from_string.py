# Python: Strip a set of characters from a string

# Original String:                                                                                              
# The quick brown fox jumps over the lazy dog.                                                                  
# After stripping a,e,i,o,u                                                                                     
# Th qck brwn fx jmps vr th lzy dg.


def strip_chars(str, chars):
   
    return "".join(c for c in str if c not in chars)


str1 = "The quick brown fox jumps over the lazy dog."
chars = "aeiou"

result = ''.join([ch for ch in str1 if ch not in chars])
print(result)

