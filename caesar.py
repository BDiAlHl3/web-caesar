import string
def rotate_character(char,rot):
    """ Rotate any char (alpha or non-alpha) right by rot positions """
    rtn_obj = ""
    if alphabet_position(char)<0: # return char if it is not alphabetic
        return char
    new_pos = alphabet_position(char)+rot
    if new_pos > 12:
        new_pos = new_pos%26

    if char.isupper():
        rtn_obj = string.ascii_uppercase[new_pos]
    else:
        rtn_obj = string.ascii_lowercase[new_pos]

    return rtn_obj

def alphabet_position(letter):
    """ Return letter's position in the alphabet """
    #  Determine letter position in alphabet
    index = (string.ascii_lowercase).find(letter) # is letter lowercase ?
    if index<0:
        index = (string.ascii_uppercase).find(letter) # is letter uppercase ?
#    print(index)
    index=int(index)
    return index

def encrypt(text,rot):
    """ Encrypt text, rotating characters to the right by rot positions """
    new_text=""
    for x in range(0,len(text)):
        new_text=new_text+rotate_character(text[x],rot)
    return new_text
