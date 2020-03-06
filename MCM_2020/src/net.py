from word2vec import load_model
# from torch import nn, Tensor
from utils import MyData

if __name__ == "__main__":
    data = MyData('1.tsv')
    # train_data = data.train_data()
    # test_data = data.test_data()

    # def collate_fn(batch):
    #     sentence_matrix = [list_to_one_hot(item[0]) for item in batch]
    #     labels = [item[1] for item in batch]
    #     labels = torch.Tensor(labels).long()
    #     return [sentence_matrix,labels]

    # train_loader = DataLoader(train_data, batch_size=128, shuffle=True,collate_fn=collate_fn)
    # test_loader = DataLoader(test_data, batch_size=128, shuffle=True,collate_fn=collate_fn)
