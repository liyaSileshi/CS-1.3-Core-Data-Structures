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
                return pattern_index

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
