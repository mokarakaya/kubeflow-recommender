import pandas as pd
import datetime
import pickle
import scipy.sparse as sp
import numpy as np
from lightfm import LightFM

class ModelBuilder:
    def __init__(self, source_file):
        self.source_file = source_file

    def build(self):
        print('start', datetime.datetime.now())
        df = pd.read_csv(self.source_file)
        number_of_users = df['user_id'].max()
        number_of_items = df['item_id'].max()
        train = sp.coo_matrix((df['rating'], (df['user_id'], df['item_id'])))
        # Load the MovieLens 100k dataset. Only five
        # star ratings are treated as positive.
        # data = fetch_movielens(min_rating=5.0)

        # Instantiate and train the model
        model = LightFM(loss='warp')
        model.fit(train, epochs=30, num_threads=2)
        prediction = model.predict(np.array([3]),np.array([2]))
        print(prediction)
        pickle.dump(model, open('lightfm.p', 'wb'))
        # Evaluate the trained model
        # test_precision = precision_at_k(model, data['test'], k=5).mean()
        # print(test_precision)
        return model