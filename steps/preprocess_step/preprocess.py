from steps.preprocess_step.preprocessor import Preprocessor

pre = Preprocessor('test/u.data', 'test/preprocessed.csv')
df = pre.process()
assert df.columns.size == 3