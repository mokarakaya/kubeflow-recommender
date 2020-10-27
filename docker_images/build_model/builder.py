import pandas as pd
from surprise import SVD, Reader
from surprise.dataset import DatasetAutoFolds
from surprise.dataset import Dataset
from surprise.model_selection import cross_validate
from docker_images.build_model.util import train_test_split
import datetime
import pickle
class ModelBuilder:
    def __init__(self, source_file):
        self.source_file = source_file

    def build(self):
        print('start', datetime.datetime.now())
        df = pd.read_csv(self.source_file)
        number_of_users = df['user_id'].max()
        number_of_items = df['item_id'].max()
        # df = df.drop(columns=['timestamp'])
        train, test = train_test_split(df)
        print('df loaded', datetime.datetime.now())
        train_data = Dataset.load_from_df(train, Reader())
        trainset = train_data.build_full_trainset()

        print('data loaded', datetime.datetime.now())

        print('trainset crated', datetime.datetime.now())
        # data = Dataset.load_builtin('ml-100k')
        # df_train, df_test = train_test_split(df)
        # train = DatasetAutoFolds(df=df_train)
        # test = DatasetAutoFolds(df=df_test)

        # We'll use the famous SVD algorithm.
        algo = SVD()
        print('fit started', datetime.datetime.now())
        algo.fit(trainset)
        print('fit done', datetime.datetime.now())
        prediction = algo.predict(1,3)
        print(prediction)
        print('prediction done', datetime.datetime.now())
        # algo.fit(train)
        # algo.test(test)
        # Run 5-fold cross-validation and print results
        pickle.dump(algo, open('svd.p', 'wb'))
        # results = cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
        # print(results)
        return algo