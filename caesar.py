alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
             'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        postiton = alphabet.index(letter)
        new_postion = postiton + shift_amount
        new_letter = alphabet[new_postion]
        cipher_text += new_letter
    print(f"The encoded string is: {cipher_text}")



def decrypt(cypher_text, shift_amount):
    plain_text = ''
    for letter in cypher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(f"The decoded string is: {plain_text}")


if direction == "encode":
    encrypt(text, shift)
else:
    decrypt(text, shift)