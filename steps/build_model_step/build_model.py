from steps.build_model_step.lightfm_builder import ModelBuilder

model_builder = ModelBuilder('test/preprocessed.csv')
algo = model_builder.build()
assert algo is not None