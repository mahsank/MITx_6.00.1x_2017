'''
The Message class contains methods that could be used to apply a cipher to a
string, either to encrypt or to decrypt a message (since for Caesar codes this
is the same action).

In the next two questions, you will fill in the methods of the Message class
found in ps6.py according to the specifications in the docstrings. The methods
in the Message class already filled in are:

__init__(self, text) The getter method get_message_text(self) The getter method
get_valid_words(self), notice that this one returns a copy of self.valid_words
to prevent someone from mutating the original list.  In this problem, you will
fill in two methods:

Fill in the build_shift_dict(self, shift) method of the Message class. Be sure
that your dictionary includes both lower and upper case letters, but that the
shifted character for a lower case letter and its uppercase version are lower
and upper case instances of the same letter. What this means is that if the
original letter is "a" and its shifted value is "c", the letter "A" should
shift to the letter "C".

If you are unfamiliar with the ordering or characters of the English alphabet,
we will be following the letter ordering displayed by string.ascii_lowercase
and string.ascii_uppercase:

>>> import string
>>> print(string.ascii_lowercase)
abcdefghijklmnopqrstuvwxyz
>>> print(string.ascii_uppercase)
ABCDEFGHIJKLMNOPQRSTUVWXYZ

A reminder from the introduction page - characters such as the space character,
commas, periods, exclamation points, etc will not be encrypted by this cipher -
basically, all the characters within string.punctuation, plus the space (' ')
and all numerical characters (0 - 9) found in string.digits.

Fill in the apply_shift(self, shift) method of the Message class. You may find
it easier to use build_shift_dict(self, shift). Remember that spaces and
punctuation should not be changed by the cipher. Also remember that the
shifting down the alphabet means to shift "right-ward" towards letters further
down in the alphabet..zip

'''

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        # length of the key should be in between 0 and 25
        self.shift = shift
        assert self.shift >=0 and self.shift < 26
        # reference string containing upper and lower case letters
        letters = [string.ascii_uppercase, string.ascii_lowercase]
        dictionary = {}
        for k in range(len(letters)):
            ref_str = letters[k]
            for char in ref_str:
                index = ref_str.find(char)
                index += self.shift
                if index >= len(ref_str):
                    index -= len(ref_str)
                elif index < 0:
                    index += len(ref_str)
                dictionary[char] = ref_str[index]
        return dictionary

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        special_chars = string.punctuation + string.digits + ' '
        dictionary = self.build_shift_dict(shift)
        ciphered_msg =''
        for char in self.message_text:
            if char in special_chars:
                ciphered_msg += char
            else:
                ciphered_msg += dictionary[char]
        return ciphered_msg
