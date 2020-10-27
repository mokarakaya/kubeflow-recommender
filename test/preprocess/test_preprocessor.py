from docker_images.preprocess.preprocessor import Preprocessor

def test_process():
    pre = Preprocessor('test/u.data', 'test/preprocessed.csv')
    df = pre.process()
    assert df.columns.size == 3
