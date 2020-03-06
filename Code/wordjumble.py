import timeit
from hashtable import HashTable

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
        sum = 0
        for j in jumble_word:
            sum += ord(j)
        print(sum)
        # print(len(jumble_word))
    
    for w in word_list:
        sum_dict = 0
        #  and sorted(w)==sorted(jumble_word)
        if len(w) == len(jumble_word) and sorted(w) == sorted(jumble_word): #if the word in the dictionary have same length as jumble word
            for i in w:
                sum_dict += ord(i)
            if sum == sum_dict: #if sum of the word is equal to sum of dict word
                new_list.append(w)#append dictionary to new list


    # print(word)
    # print(word_list)
    # print(ord('a'))
    print(new_list)
    return word_list

unjumble('tefon')

 

 