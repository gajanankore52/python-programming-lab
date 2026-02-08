# Remove empty tuples from a list - Python

#Using list comprehension

# a = [(1, 2), (), (3, 4), (), (5,)]

# RES = [t for t in a if t]

# print(RES)

# ===================================


# a = [(1, 2), (), (3, 4), (), (5,)]

# # Using for loop

# res = []

# for t in a:
    # if len(t) > 0:
        # res.append(t)

# print(res)
# =======================e==

#Using Filter

a = [(1, 2), (), (3, 4), (), (5,)]

res = list(filter(None,a))

print(res)