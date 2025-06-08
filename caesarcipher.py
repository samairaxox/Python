alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_no, encode_decode):
    og_text = ""
    for letter in original_text:
        if letter not in alphabets:
            og_text += letter
        else:
            if encode_decode == "decode":
                shift_no *= -1
            shifted_posn = alphabets.index(letter) + shift_no
            shifted_posn %= len(alphabets)
            og_text += alphabets[shifted_posn]
    print(f"Here is the {encode_decode}: {og_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type your shift number:\n"))

    caesar(text, shift, direction)

    restart = input("Type 'yes' to continue and 'no' to finish:\n").lower()
    if restart == "no":
        should_continue = False

print("All done")
