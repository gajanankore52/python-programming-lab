# Check if element exists in list in Python

def check_existance(target,data_list):
    # 1. Standard check (Fast for small/medium lists)
    if target in data_list:
        return True
    
    # 2. Performance optimization for massive lists
    # data_set= set(data_list)
    # return target in data_set
    return False


def main():
    numbers = [10, 20, 30, 40, 50]
    search_val = 30

    # Using an f-string for a cleaner print statement
    result_msg = "exists in" if check_existance(search_val,numbers) else "does not exist in"
    print(f'Element {search_val} {result_msg} the list.')
if __name__ =="__main__":
    main()