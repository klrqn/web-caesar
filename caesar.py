import string
UPPERASCII = 65
LOWERASCII = 97
alpha = string.ascii_letters
alphaL = string.ascii_lowercase
alphaU = string.ascii_uppercase

def alphabet_position(letter):
    if letter in alphaU:
        # num = alphaU[ord(letter)-65]
        num = ord(letter)-UPPERASCII
        return num
    if letter in alphaL:
        # num = alphaL[ord(letter)-97]
        num = ord(letter)-LOWERASCII
        return num
    return letter

def rotate_character(char, rot):
    if char in alpha:
        position = alphabet_position(char)
    else:
        return char
    rotatedNum = (position + rot) % 26

    if char in alphaU:
        return chr(rotatedNum + UPPERASCII)
    if char in alphaL:
        return chr(rotatedNum + LOWERASCII)
    else:
        return char

def encrypt(text, rot):
    encryptedText = ""
    for eachChar in text:
        if eachChar in alpha:
            encryptedText = encryptedText + rotate_character(eachChar, rot)
        else:
            encryptedText = encryptedText + eachChar
    return encryptedText
