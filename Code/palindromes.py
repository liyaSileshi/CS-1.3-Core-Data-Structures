#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    # print(clean(text))
    text = clean(text)
    return is_palindrome_recursive(text, left=0, right=len(text)-1)


def is_palindrome_iterative(text):
    word = clean(text)
    left = 0
    right = len(word) - 1
    while(left <= right): #while there are characters to compare
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def clean(text):
    word = ''
    for i in text.lower(): #to clean the text from punctuation, whitespace, CAPs
        if i in string.ascii_lowercase:
            word += i
    return word

def is_palindrome_recursive(text, left=None, right=None):
    word = clean(text)
    if len(word) <= 1: #if there is only one letter or no letter at all
        return True

    if abs(left - right) <= 1: #if the index is the same or side by side
        if word[left] == word[right]:
            return True
        else:
            return False

    if left <= right: #not crossing eachother
        if word[left] == word[right]:
            return is_palindrome_recursive(word, left+1, right-1)
        else:
            return False

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')

if __name__ == '__main__':
    # main()
    text = 'ABC' 
    word = clean(text)
    # print(is_palindrome_iterative('Racecar'))
    print(is_palindrome_recursive(word, 0, len(word)-1))
