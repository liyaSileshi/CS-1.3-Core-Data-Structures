#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    flag = None
    # pattern_index = 0
    first_pattern = 0
    pattern_index = []
    if pattern == '': #all strings contain empty string
        return True

    for i in range(len(text)):
        if text[i] == pattern[0]:
            if len(pattern) == 1: #only one ch in pattern
                first_pattern = 0
                return True
            for j in range(1, len(pattern)):
                if i+j >= len(text):
                    break
                elif text[i+j] == pattern[j]:
                    flag = True
                    first_pattern += 1
                else:
                    
                    flag = False
                    break

    if flag == None: #no pattern found at all, doesn't go to the nested loop
        return False

    if first_pattern >= len(pattern) - 1: #atleast one pattern is found
        flag = True

    return flag

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)

    if contains(text, pattern):
        return text.index(pattern)
    
def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    pattern_index = []
    if pattern == '': #all strings contain empty string
        for i in range(len(text)):
            pattern_index.append(i) #appends all index
        return pattern_index

    if contains(text, pattern): 
        # return [i for i in range(len(text)) if text.startswith(pattern, i)]
        for i in range(len(text)):
            if text.startswith(pattern, i): #second paramenter specifies start of search
                pattern_index.append(i)
        return pattern_index

    else:
        return [] #if pattern not in text


    # if contains(text, pattern):       
    #     pattern_index.append(text.index(pattern))
    #     # find_index()
    #     # return text.index(pattern)
    #     return pattern_index
    # return pattern_index

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
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
    # print(contains('abra cadabra', 'adab'))
    print(find_all_indexes('aaa', 'a'))
