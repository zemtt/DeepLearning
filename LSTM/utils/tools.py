
import json
from torch import zeros, cat, LongTensor

# with open('./word_dict.json') as f:
#     word_dict = json.load(f)

word_dict = {}
for i in range(21283):
    word_dict[i] = 1


def sentence_split(x):
    words_list = []
    cur_word = ''
    for char in x:
        if char in '1234567890':
            if cur_word:
                if cur_word[-1] in '1234567890':
                    cur_word += char
                else:
                    words_list.append(cur_word)
                    cur_word = char
            else:
                cur_word += char
        elif char in 'zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP':
            if cur_word:
                if cur_word[-1] in 'zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP':
                    cur_word += char
                else:
                    words_list.append(cur_word)
                    cur_word = char
            else:
                cur_word += char
        elif char == ' ':
            if cur_word:
                words_list.append(cur_word)
                cur_word = ''
        else:
            if cur_word:
                words_list.append(cur_word)
                cur_word = ''
            words_list.append(char)
    if cur_word:
        words_list.append(cur_word)
    return words_list


def sentence_to_list(sentence):
    sentence_l = []
    for word in sentence_split(sentence):
        sentence_l.append(
            word_dict[word] if word in word_dict else(len(word_dict)))
    return sentence_l


def word_to_vector(word):
    num = word_dict[word] if word in word_dict else(len(word_dict))
    result = zeros(len(word_dict)+1).reshape(1, len(word_dict)+1)
    result[0][num] = 1
    return result


def sentence_to_matrix(sentence):
    sentence_m = None
    for word in sentence_split(sentence):
        word_v = word_to_vector(word)
        if sentence_m != None:
            sentence_m = cat((sentence_m, word_v), 0)
        else:
            sentence_m = word_v
    return sentence_m


def list_to_one_hot(lis):
    dim = len(lis)
    lis = LongTensor([lis])
    one_hot = zeros(len(word_dict)+1, dim)
    one_hot = one_hot.scatter(0, lis, 1)
    return one_hot
