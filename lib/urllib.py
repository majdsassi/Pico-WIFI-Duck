def url_decode(encoded_string):
    decoded_string = ""
    i = 0
    while i < len(encoded_string):
        if encoded_string[i] == '%':
            # Extract the hexadecimal value and convert it to a character
            decoded_char = chr(int(encoded_string[i + 1:i + 3], 16))
            decoded_string += decoded_char
            i += 3  # Move to the next encoded character
        else:
            # If not encoded, keep the character as it is
            decoded_string += encoded_string[i]
            i += 1
    return decoded_string
