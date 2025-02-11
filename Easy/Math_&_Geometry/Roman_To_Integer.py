def roman_to_int(s):
    """
    Convert a Roman numeral string to an integer.
    """
    # Create a dictionary mapping Roman numerals to their corresponding integer values.
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    # Initialize three variables: previous, current, and result.
    # previous will hold the value of the previous Roman numeral.
    # current will hold the value of the current Roman numeral.
    # result will hold the cumulative sum.
    previous = 0
    current = 0
    result = 0
    
    # Iterate through the characters in the string from right to left.
    for i in range(len(s) - 1, -1, -1):
        current = roman_dict[s[i]]
        
        # If the current value is less than the previous value,
        # that means we have something like 'IV' where we need to subtract the smaller number.
        if current < previous:
            result -= current
        else:
            # Otherwise, we just add the current value to the result.
            result += current
        
        # Update the previous value to be the current value for the next iteration.
        previous = current
    
    return result