import sys, os

sys.path.insert(0, 'kubeflow-recommender/')

from steps.build_model_step.lightfm_builder import ModelBuilder

model_builder = ModelBuilder('kubeflow-recommender/test/preprocessed.csv')
algo = model_builder.build()
assert algo is not None