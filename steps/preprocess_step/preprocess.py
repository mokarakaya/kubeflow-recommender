import sys

sys.path.insert(0, 'kubeflow-recommender/')

from steps.preprocess_step.preprocessor import Preprocessor

pre = Preprocessor('kubeflow-recommender/test/u.data', 'kubeflow-recommender/test/preprocessed.csv')
df = pre.process()
assert df.columns.size == 3