#Accept array from user and check whether array is sorted or not


def is_sorted(ilist):
    # Using all() with a generator expression for a clean, one-line check
    # We check if every element is less than or equal to the next one
   
    return all(ilist[i] <= ilist[i+1] for i in range(len(ilist) -1))

def main():
    
    try:
    
        n= int(input('Enter number of elements: '))
    
        print(f'Enter {n} Numbers: ')    
        # Using list comprehension for cleaner input

        arr = [int(input()) for _ in range(n)]

        if is_sorted(arr):
            print('The list is sorted in ascending order.')
        else:
            # Check for descending order as a bonus
            if all(arr[i] >= arr[i+1] for i in range(len(arr)-1)):
                print("The list is sorted in descending order.")
            else:
                print('The list is NOT sorted.')

    except ValueError:
        print('Invalid input! Please enter integers only.')


if __name__ == '__main__':
    main()