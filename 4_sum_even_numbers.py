def addition_of_even(arr):
    return sum(x for x in arr if x % 2 == 0)

def main():
    # 1. Ask ONCE for the total amount of numbers
    try:
        count = int(input("How many numbers do you want to enter: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    # 2. The list comprehension runs exactly 'count' times
    # 'i' goes from 0 to (count - 1)
    list1 = [int(input(f'Enter number {i+1}: ')) for i in range(count)]
        
    iResult = addition_of_even(list1)
    print('Addition of even numbers is:', iResult)

if __name__ == "__main__":
    main()