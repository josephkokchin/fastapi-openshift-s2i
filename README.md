# ML Service Deployment via FastAPI - OpenShift S2I Method
 In this example, OpenShift S2I uses a Builder image and its sources to create a new Docker image that is deployed to the OpenShift cluster. 

 ## Installation
 pip install -r requirements

 ## Running the App
 1. Start the app with:
 ```bash
uvicorn app:app --reload
 ```

Or
 ```bash
python3 app.py
 ```

 2. Go to http://0.0.0.0:8080/docs.
