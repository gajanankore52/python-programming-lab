# Python program to interchange first and last elements in a list

# my_list = [1, 2, 3, 4, 5]

# my_list[-1],my_list[0] = my_list[0],my_list[-1]

# print(my_list)

#===============================



#Interchange first and last elements using Temporary Value

# def swapList(newList):
    
    # size = len(newList)
    
    # temp = newList[0]
    # newList[0]=newList[size-1]
    # newList[size-1] = temp
    
    # return newList

# newList = [12, 35, 9, 56, 24]

# print(swapList(newList))

#================================

#Swapping first and last items in a list using tuple variable

# def swapList(list):
    
    
    # get = list[-1],list[0]
    
    # list[0],list[-1]=get
    
    # return list


# newList = [12, 35, 9, 56, 24]
# print(swapList(newList))
#=====================


# def swapList(list):
    
    # start, *middle, end = list
    # list = [end, *middle, start]
    
    # return list
    
# # Driver code
# newList = [12, 35, 9, 56, 24]

# print(swapList(newList))
#=================================================

