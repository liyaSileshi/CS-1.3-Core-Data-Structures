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
    word_list = [] #will have the list of all the dictionary words
    new_list = dict() #create a dictionary
    with open("/usr/share/dict/words", "r") as file:
        all_word = file.read().lower()
        words = all_word.split('\n')
        for word in words:
            word_list.append(word)

    for word in jumble_word: #looping over the jumble_word list
        possible_words = [] 
        for dict_word in word_list: 
            #if the word in the dictionary have same length as jumble word
            if len(dict_word) == len(word) and sorted(dict_word) == sorted(word.lower()): 
                possible_words.append(dict_word)
            new_list[word] = possible_words #dictionary to new list
    print(new_list)
    return new_list

if __name__ == '__main__':
    word1 = ['TEFON', 'SOKIK', 'NIUMEM', 'SICONU']
    pick1 = [[2,4], [0,1,3], [4], [3,4]]
    word2 = ['laurr', 'laisa', 'bureek','prouot']
    unjumble(word2)
    unjumble(word1)
