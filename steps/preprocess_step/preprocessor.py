import pandas as pd


class Preprocessor:
    def __init__(self, source_filename, target_filename):
        self.source_filename = source_filename
        self.target_filename = target_filename

    def process(self):
        df = pd.read_csv(self.source_filename, delimiter='\t')
        df.columns = ['user_id', 'item_id', 'rating', 'timestamp']
        df = df.drop(columns=['timestamp'])
        df.to_csv(self.target_filename, index=False)
        return df