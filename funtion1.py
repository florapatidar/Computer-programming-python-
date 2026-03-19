def count_lower_upper(s):

    upper_count = 0
    lower_count = 0
    
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
            
    return {'uppercase': upper_count, 'lowercase': lower_count}

input_string =input("enter a string:")
result = count_lower_upper(input_string)
print(result)
