import json
import csv
from .tools import sentence_to_matrix, sentence_to_list, list_to_one_hot
import pickle
import os


class MyData(object):
    sample_num = 0
    data_path = ''
    all_data = []

    def trans_data(self):
        with open(self.data_path, 'r') as f:
            f_csv = list(csv.reader(f))
            print(len(f_csv))
            self.sample_num = len(f_csv) - 1
            for row in f_csv[1:]:
                print(row)
                self.all_data.append(
                    [sentence_to_list(row[1]), 1 if row[2] == 'Positive' else 0])

        with open('./data.pkl', 'wb') as f:
            pickle.dump((self.all_data), f)

    def __init__(self, data_path):
        self.data_path = data_path
        if os.path.isfile('data.pkl'):
            with open('./data.pkl', 'rb') as f:
                self.all_data = pickle.load(f)
        else:
            self.trans_data()
        self.sample_num = len(self.all_data)

    def train_data(self):
        return self.all_data[self.sample_num//5:]

    def test_data(self):
        return self.all_data[:self.sample_num//5]
