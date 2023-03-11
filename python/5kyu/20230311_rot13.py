# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

# My ideas:
# Use ord and chr to increase the unicode by 13
# special characters should stay the same, so only ASCII upper and lower should change
# Unicode is char # +96
print(ord('Z'))
print(chr(122))

# a is 97 and z is 122
# A is 65 and Z is 90
# Add 13 and subtract 26 if num in > 122

def rot13(message):
    new_mess = ''
    for letter in message:
        if letter.islower():
            new_let = ord(letter) + 13
            if new_let > 122:
                new_let -= 26
            new_mess += chr(new_let)
        elif letter.isupper():
            new_let = ord(letter) + 13
            if new_let > 90:
                new_let -= 26
            new_mess += chr(new_let)
        else:
            new_mess += letter
    return new_mess


print(rot13('aA bB zZ 1234 *!?%'))