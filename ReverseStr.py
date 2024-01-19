def reverse_string(input_str):
    """
    Reverse a given string.

    Parameters:
    - input_str (str): The input string.

    Returns:
    - str: The reversed string.
    """
    reversed_str = input_str[::-1]
    return reversed_str

# Example usage:
input_string = "Concatenation"
result_reverse = reverse_string(input_string)
print(result_reverse)
