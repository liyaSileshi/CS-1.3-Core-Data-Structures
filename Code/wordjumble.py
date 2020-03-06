import timeit


import time
def timer(func):
    def _timer(*args):
        start_time = time.time()
        res = func(*args)
        end_time = time.time()
        print(end_time - start_time)
        return res
    return _timer

@timer
def unjumble(jumble_word):
    word_list = []
    new_list = dict()
    with open("/usr/share/dict/words", "r") as file:
        all_word = file.read().lower()
        words = all_word.split('\n')
        for w in words:
            word_list.append(w)
    for word in jumble_word:
        possible_words = []
        for w in word_list:
            if len(w) == len(jumble_word) and sorted(w) == sorted(jumble_word): #if the word in the dictionary have same length as jumble word
                possible_words.append(w)
            new_list[jumble_word] = possible_words #dictionary to new list

    print(new_list)
    return word_list

if __name__ == '__main__':
    unjumble(['laurr', 'laisa', 'bureek','prouot'])
