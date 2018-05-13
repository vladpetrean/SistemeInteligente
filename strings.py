def is_lower(user_string):
    # For each character...
    for char in user_string:
        # ...if it's a capital letter...
        if 'A' <= char <= 'Z':
            # return false, ending the function.
            return False

    # If we reach this, there were no capital letters.
    return True