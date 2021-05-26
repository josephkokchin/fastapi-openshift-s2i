from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from pydantic import BaseModel
import joblib

class IrisSpecies(BaseModel):
    sepal_length: float 
    sepal_width: float 
    petal_length: float 
    petal_width: float


class IrisModel:
    def __init__(self):
        self.iris = load_iris()
        self.model_fname_ = 'sample_model/iris_model.pkl'
        try:
            self.model = joblib.load(self.model_fname_)
        except Exception as _:
            self.model = self._train_model()
            joblib.dump(self.model, self.model_fname_)
        

    def _train_model(self):
        X = self.iris.data
        y = self.iris.target
        rfc = RandomForestClassifier()
        model = rfc.fit(X, y)
        return model

    def predict_species(self, sepal_length, sepal_width, petal_length, petal_width):
        data_in = [[sepal_length, sepal_width, petal_length, petal_length]]
        class_idx = self.model.predict(data_in)[0]
        prediction = self.iris.target_names[class_idx]
        probability = self.model.predict_proba(data_in).max()
        return prediction, probability
