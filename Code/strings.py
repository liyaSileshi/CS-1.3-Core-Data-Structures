#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text.
    Runtime: O(t*p) needs to go through each letter in text and pattern to check
    if pattern occurs and if it also occurs multiple times. (since contains function
    uses find_all_indexes method)
    Space complexity: O(t)
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    
    return find_all_indexes(text, pattern) != []

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.
    Runtime: O(t*p) needs to go through each letter in text and pattern to check
    if pattern occurs and if it also occurs multiple times. (since contains function
    uses find_all_indexes method)
    Space complexity: O(t)
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    
    return self.find_all_indexes[0]
    
def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    Runtime: O(t*p) needs to go through each letter in text and pattern to check
    if pattern occurs and if it also occurs multiple times.
    Space complexity: O(t)
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    pattern_index = []
    flag = None
    first_pattern = 0
    index_stop = len(text) - len(pattern) + 1 #to not include indexes that will not be compared

    if pattern == '': #all strings contain empty string
        for i in range(len(text)): #worst case for space complexity
            pattern_index.append(i) #appends all index
        return pattern_index

    for i in range(index_stop):
        if text[i] == pattern[0]:
            if len(pattern) == 1:
                pattern_index.append(i)
            for j in range(1, len(pattern)):
                if i+j >= len(text):
                    break
                elif text[i+j] == pattern[j]:
                    index_stop += 1
                    if len(pattern)-1 == j: #check if we're at the end of the pattern
                        pattern_index.append(i)
                else:
                    break
                 
    return pattern_index


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    # main()
    # print(contains('abc', 'bcd'))
    # print(find_all_indexes('hahahahaha', 'haha'))
    print(find_index('c', 'cde'))