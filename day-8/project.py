# WAP to encrypt and decrypt the message

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(message, shift):
    cypher_text = ""
    for letter in message:
        pos = alphabet.index(letter)
        new_pos = pos + shift
        new_letter = alphabet[new_pos]
        cypher_text += new_letter
    print("\nEncrypted message is:",cypher_text)

dir = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
message = input("\nType yor message:\n").lower()
shift = int(input("\nType the shift number:\n"))

if dir == "encode":
    encode(message = message, shift = shift)
