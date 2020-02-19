#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text.
    Runtime: Best Case - O(p)- if the pattern is found at the beginnning of the text
    Worst Case- O(n*p)- if pattern not found, or found at the end of the text"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # flag = None
    # first_pattern = 0
    # index_stop = len(text) - len(pattern) + 1 #to not include indexes that will not be compared
    # if pattern == '': #all strings contain empty string
    #     return True 

    # for i in range(index_stop):
    #     if text[i] == pattern[0]:
    #         if len(pattern) == 1: #only one ch in pattern
    #             first_pattern = 0
    #             return True
    #         for j in range(1, len(pattern)):
    #             if i+j >= len(text):
    #                 break
    #             elif text[i+j] == pattern[j]: #compare pattern index to text index
    #                 flag = True
    #                 first_pattern += 1 
    #                 index_stop += 1 #increment the range of indexes
    #             else:
    #                 flag = False
    #                 break

    # if flag == None: #no pattern found at all, doesn't go to the nested loop
    #     return False

    # if first_pattern >= len(pattern) - 1: #atleast one pattern is found
    #     flag = True

    # return flag
    return find_all_indexes(text, pattern) != []

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.
    Runtime: Best Case - O(p)- if the pattern is found at the beginnning of the text
    Worst Case- O(t*p)- if pattern not found, or found at the end of the text
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if contains(text, pattern):
        return text.index(pattern)
    
def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    Runtime: O(t*p)"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    pattern_index = []
    flag = None
    first_pattern = 0
    index_stop = len(text) - len(pattern) + 1 #to not include indexes that will not be compared

    if pattern == '': #all strings contain empty string
        for i in range(len(text)):
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
                    if len(pattern)-1 == j:
                        pattern_index.append(i)
                else:
                    break
                 
    # else:
    return pattern_index #if pattern not in text


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
