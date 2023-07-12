from art import logo


# Create list of alphabet charecters to later produce an encoded/decoded copy of entered string 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
             'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Print Caesar Cipher logo
print(logo)

# Gather required information from user

#Cipher direction
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

# User text to be encoded or decoded
text = input("Type your message:\n").lower()

# Amount to shift 
shift = int(input("Type the shift number:\n"))

def caesar(cipher_direction, entered_text, shift_amount):
    # Create string buffer to store converted string 
    text_buffer = ""
    
    # Check whether encode or decode is selected
    if cipher_direction == "decode":
        shift_amount *= -1
    
    # Iterate over each letter, shift letter in alpha list, return converted letter, add to string buffer
    for letter in entered_text:
        postion = alphabet.index(letter)
        new_position = postion + shift_amount
        text_buffer += alphabet[new_position]
    
    # Print the result
    print(f"The {cipher_direction}d string is: {text_buffer}")





# Run code
if __name__ == "__main__":
    caesar(direction, text, shift)



# OLD CODE FOR REFERENCE

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         postiton = alphabet.index(letter)
#         new_postion = postiton + shift_amount
#         new_letter = alphabet[new_postion]
#         cipher_text += new_letter
#     print(f"The encoded string is: {cipher_text}")



# def decrypt(cypher_text, shift_amount):
#     plain_text = ''
#     for letter in cypher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(f"The decoded string is: {plain_text}")


# if direction == "encode":
#     encrypt(text, shift)
# else:
#     decrypt(text, shift)