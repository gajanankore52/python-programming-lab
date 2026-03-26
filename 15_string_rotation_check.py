# Python - Check if two strings are Rotationally Equivalent

def are_rotations(s1, s2):
    # 1. Check if lengtjs are equal (seesential first step)
    if len(s1) != len(s2):
        return False

    # 2. Check if s2 is a substring of (s1 + s2)
    # This covers all possible rotations in one check
    return s2 in (s1 + s2)

def main():
    str1 = 'geeks'
    str2 = 'eksge'    

    if are_rotations(str1,str2):
        print(f"'{str2}' is a rotation of '{str1}'")
    else:
        print(f"'{str2}' is NOT a rotation of '{str1}'")

if __name__ == "__main__":
    main()
   
                

