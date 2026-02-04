# Check if element exists in list in Python


a = [10, 20, 30, 40, 50]

print("Element exists in the list") if 30 in a else print("Element does not exist")
# ==================================================


#Using a loop

# a = [10, 20, 30, 40, 50]

# num = 80
# flag = False

# for val in a:
    # if num == val:
        # flag=True
        # break
        
# print("Element exists in the list") if flag else print("Element does not exist")

# ================================


# Using any()


a = [10, 20, 30, 40, 50]

# flag = any(x==30 for x in a)

print("Element exists in the list") if any(x==30 for x in a) else print("Element does not exist")