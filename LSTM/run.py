import csv
import json
from utils.tools import sentence_split, word_to_vector, sentence_to_matrix
from utils.MyData import MyData

data_path = './wbqg3541/train.csv'


def dump_word_dict():
    word_bag = []
    with open(data_path, 'r') as f:
        f_csv = list(csv.reader(f))
        print(len(f_csv))
        for row in f_csv[1:]:
            word_bag.extend(sentence_split(row[1]))
    word_bag = list(set(word_bag))
    print(len(word_bag))

    word_dict = {}
    for i in range(len(word_bag)):
        word_dict[word_bag[i]] = i

    with open('./utils/word_dict.json', 'w') as f:
        json.dump(word_dict, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    # dump_word_dict()
    # print(sentence_to_matrix('Nice baby apny baba ki tarah,Positive').size())
    data = MyData(data_path)
