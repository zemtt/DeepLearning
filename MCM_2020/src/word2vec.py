from gensim.models import Word2Vec, word2vec
from data_loader import load_data
import os

data_path = '../Data'


def extract_review(data):
    result = ""
    for each in data:
        result += each[-3] + ' ' + each[-2] + '\n'
    return result


def dump_sentences(file_name):
    data = load_data(file_name)
    with open(os.path.join(data_path, 'sentences', file_name.split('.')[0] + '.txt'), 'w') as f:
        f.write(extract_review(data))


def dump_all_sentences():
    data = []
    for each in '123':
        data.extend(load_data(each + '.tsv'))
    with open(os.path.join(data_path, 'sentences', 'all_review.txt'), 'w') as f:
        f.write(extract_review(data))


def train_model_and_save():
    sentences = word2vec.LineSentence(
        os.path.join(data_path, 'sentences', 'all_review.txt'))
    model = Word2Vec(sentences, size=100, window=10, min_count=1, workers=4)
    model.save(os.path.join(data_path, 'model'))


def load_model():
    model = Word2Vec.load(os.path.join(data_path, 'model'))
    return model


if __name__ == "__main__":
    model = load_model()
    for i in model.wv.most_similar("newborn"):
        print(i)
