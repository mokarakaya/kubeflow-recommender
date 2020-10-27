import json
import os
import pickle
import numpy as np


class MyPredictor(object):
    def __init__(self, model):
        """Stores artifacts for prediction. Only initialized via `from_path`.
        """
        self._model = model

    def predict(self, instances, **kwargs):
        user_id, item_id = instances
        outputs = self._model.predict(np.array([user_id]), np.array([item_id]))
        return json.dumps(outputs.tolist())

    @classmethod
    def from_path(cls, model_dir):
        model_path = os.path.join(model_dir, 'lightfm.p')
        with open(model_path, 'rb') as f:
        # with open('lightfm.p', 'rb') as f:
            model = pickle.load(f)

        return cls(model)

# predictor = MyPredictor.from_path('')
# preditions = predictor.predict([2,3])
# print(preditions)