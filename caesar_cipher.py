from art import logo

print(f"{logo}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
            'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z']


# combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "encode": #We can choose to remove this line of code though
        shift_amount = shift_amount
    elif cipher_direction == "decode":
        shift_amount *= -1 #Enables it remain -ve in order to subtract
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char) #index search
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            # the shift won't apply for non-alphabetic characters
            #this helps encourage spacings and special characters 
            end_text += char 
    print(f"Here's the {direction}d message: \n{end_text}")


reload_code = True
while reload_code == True:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number: "))
    #This solves the issue whenever the shift amount is above 26
    shift = shift % 26
    # call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    restart_end = input("\nType 'yes' to restart, otherwise type 'no': ").lower()
    if restart_end == 'no':
        reload_code = False # stops while loop
        print("\nGoodbye!")
    #else statement is not necessary, since it will loop automatically
