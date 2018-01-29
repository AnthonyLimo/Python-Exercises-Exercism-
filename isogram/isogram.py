def is_isogram(string):
    lower_string = string.lower()
    for char in lower_string:
        if lower_string.count(char) > 1:
            if char == '-' or char == ' ':
                continue
            return False
    return True 
