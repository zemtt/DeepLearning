from data_loader import load_data
from word2vec import load_model
import random
import pickle
import os


w2v_model = load_model()


class MyData(object):
    def __init__(self, path):
        self.path = path
        self.all_data = self.load_data()
        self.sample_num = len(self.all_data)

    def load_data(self):
        if os.path.isfile('data.pkl'):
            with open('./data.pkl', 'rb') as f:
                results = pickle.load(f)
        else:
            data = load_data(self.path)
            results = []
            for each in data:
                text = each[-2] + ' ' + each[-3]
                label = int(each[-8])
                matrix = [w2v_model[each]
                          for each in text.split(' ') if each in w2v_model.wv.vocab]
                results.append([matrix, label])
            with open('./data.pkl', 'wb') as f:
                pickle.dump((results), f)
        random.shuffle(results)
        return results

    def train_data(self):
        return self.all_data[self.sample_num//5:]

    def test_data(self):
        return self.all_data[:self.sample_num//5]
