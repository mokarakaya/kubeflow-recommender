from docker_images.build_model.lightfm_builder import ModelBuilder

def test_build():
    model_builder = ModelBuilder('test/preprocessed.csv')
    algo = model_builder.build()
    assert algo is not None
