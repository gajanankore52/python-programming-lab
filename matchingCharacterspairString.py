# Python | Count the Number of matching characters in a pair of string


s1 = "VISHAKSHI"
s2 = "VANSHIKA"

# s1 = list(set(s1))
# s2 = list(set(s2))

# iCnt = 0
# for ch in s2:
    
    # if ch in s1:
        # iCnt += 1
        

# print(iCnt)

# ====================

# res = len(set(s1.lower()).intersection(set(s2.lower())))

# print(res)


# ========================================
# Using List Comprehension

s1 = "VISHAKSHI"
s2 = "VANSHIKA"




res = len([ ch for ch in set(s1.lower()) if ch in set(s2.lower())])

print(res)