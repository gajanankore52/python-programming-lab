# Reversing a List in Python


# a = [1, 2, 3, 4, 5]

# a.reverse()

# print(a)
# ====================


# a = [1, 2, 3, 4, 5]

# a = a[::-1]

# print(a)

# # ==================

# a = [1, 2, 3, 4, 5]

# a = list(reversed(a))

# print(a)

# ================================

# a = [1, 2, 3, 4, 5]


# res = []

# for val in a:res.insert(0,val)
    
# print(res)

#==========================

#Using a Loop (In-place reverse)


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(f'Original list is {a}')
# start,end = 2,6

# while start < end :
    
    # a[start],a[end] = a[end],a[start]
    
    # start += 1
    # end -= 1
    

# print(f'After reverse list is {a}')

# ========================

#Using List Comprehension


# a = [1, 2, 3, 4, 5]

# res = [a[i] for i in range(len(a)-1,-1,-1)] 

# print(res)
