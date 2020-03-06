import csv
import os
import json

data_path = '../Data'


def load_data(file_name):
    result = []
    with open(os.path.join(data_path, file_name), 'r')as f:
        f_csv = csv.reader(f, delimiter='\t', quotechar='|')
        for row in f_csv:
            result.append(row)
    return result[1:]


def list_item_to_dict(item):
    header = ['marketplace', 'customer_id', 'review_id', 'product_id',
              'product_parent', 'product_title', 'product_category', 'star_rating',
              'helpful_votes', 'total_votes', 'vine', 'verified_purchase',
              'review_headline', 'review_body', 'review_date']
    return dict(zip(header, item))


if __name__ == "__main__":
    data_1 = load_data('1.tsv')
    item = data_1[2]
    print(json.dumps(list_item_to_dict(item)))
