#Accept N number from user and reverse that array in place

def reverse_array(ilist):
    """Reverse a list in-place using two pi=ointers."""
    
    i=0
    j=len(ilist)-1
    
    while i < j:
        
        # Pythonic tuple unpacking for swapping
        ilist[i],ilist[j] =  ilist[j],ilist[i]       
        i += 1
        j -= 1
    
    return ilist


def main():
    try:
        count = int(input('Enter number of elements: '))

        # Using list comprehension for clear input
        print(f'Enter {count} numbers:')
        arr = [int(input()) for _ in range(count)]

        # We don't necessarily need iResult because it's modified in-place,
        # but returning it is fine for a functional style.
        
        reverse_array(arr)

        print(f'Reverse array is: {arr}')
    except ValueError:
        print('Invalid input! Please enter integers only.')


if __name__ == '__main__':
    main()