import uvicorn
from fastapi import FastAPI
from Model import IrisModel, IrisSpecies

app = FastAPI()
model = IrisModel()

@app.post('/predict')
def predict_species(iris: IrisSpecies):
    data = iris.dict()
    prediction, probability = model.predict_species(
        data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']
    )
    return {
        'prediction': prediction,
        'probability': probability
    }

@app.get('/')
def get_root():
    return {'message': 'Welcome to the Iris prediction API.'}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)
