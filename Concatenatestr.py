def concatenate_strings(str1, str2):
    """
    Concatenate two strings.

    Parameters:
    - str1 (str): The first input string.
    - str2 (str): The second input string.

    Returns:
    - str: The concatenated string.
    """
    concatenated_str = str1 + str2
    return concatenated_str

# Example usage:
string1 = "Hello"
string2 = "World"
result_concatenation = concatenate_strings(string1, string2)
print(result_concatenation)
