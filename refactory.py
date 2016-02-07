#!/usr/local/bin/python3

#import titletest

small_words = ('into', 'the', 'a', 'of', 'at', 'in', 'for', 'on')

def book_title(title):
    """ Takes a string and returns a title-case string.
    All words EXCEPT for small words are made title case
    unless the string starts with a preposition, in which
    case the word is correctly capitalized.
    
    >>> book_title('DIVE Into python')
    'Dive into Python'
    
    >>> book_title('the great gatsby')
    'The Great Gatsby'
    
    >>> book_title('the WORKS OF AleXANDer dumas')
    'The Works of Alexander Dumas'
    """
    
    new_title=""
    for i,word in enumerate(title.lower().split()):
        if (word not in small_words) or (i == 0):
            new_title += " " + word.capitalize()
        else:
            new_title += " " + word
    return new_title.lstrip()
        
        
def _test():
    import doctest, refactory
    return doctest.testmod(refactory)
        
if __name__ == "__main__":
    _test()
        
