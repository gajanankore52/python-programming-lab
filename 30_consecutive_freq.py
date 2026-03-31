# Consecutive characters frequency - Python

s = "aaabbccaaaa"

def group_consecutive(text):
    if not text:
        return []

    res = []
    count = 1
    
    for i in range(len(text) - 1):
        if text[i] == text[i+1]:
            count += 1
        else:
            res.append(text[i] * count)
            count = 1
            
    # Append the last tracked group
    res.append(text[-1] * count)
    return res

print(group_consecutive(s))