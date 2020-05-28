import os
import numpy as np
from fastai.basic_train import load_learner

# use absolute path to this entry file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


MODEL_DIR = os.path.join(BASE_DIR, 'data')
model_fname = 'my-fastai-model.pth'
model_learner = None

def load_model(model_directory, model_fname):
    global model_learner
    model_learner = load_learner(model_directory, model_fname)
    return

load_model(MODEL_DIR, model_fname)

def predict_query(text, model_learner = None):
    if model_learner == None:
        return {}
    preds = model_learner.predict()
    return {"predictions": preds}

def run(
    json_data={}, 
    method='POST',
    *args, 
    **kwargs):
    global model_learner
    if f"{method}".lower() != "post":
        return {"status": 400, "message": "POST method required."}
    if len(json_data.keys()) == 0:
         return {"status": 400, "message": "JSON data required."}
    query = json_data.get("query") or None
    if query == None:
        return {"status": 400, "message": "You must pass a query."}
    pred_response = predict_query(query, model_learner = model_learner)
    return pred_response