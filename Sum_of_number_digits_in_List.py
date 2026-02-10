# Sum of number digits in List in Python


# Using Loops

# a = [123, 456, 789]

# res = []

# for num in a:
    # total = 0
    
    # while num !=0:
        
        # digit = num % 10
        # total +=digit
        # num =num//10
        
    # res.append(total)
    
# print(res)

#+====================================

#Using List Comprehension

# a = [123, 456, 789]

# res = [sum(int(num1) for num1 in str(num)) for num in a]

# print(res)

#===============

#Using map Function

a = [123, 456, 789]

res = list(map(lambda val: sum(  int(digit) for digit in str(val) ),a))

print(res)

