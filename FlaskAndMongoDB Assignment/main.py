import json
import requests
from pymongo import MongoClient
from flask import Flask, jsonify
import Credentials

def logIntoDatabase():
   url = "mongodb://{}:{}@{}:{}".format(Credentials.MONGO_USER, Credentials.MONGO_PASS, Credentials.MONGO_HOST,
                                        Credentials.MONGO_PORT)
   client = MongoClient(url)
   db = client[Credentials.DATABASE_NAME]
   return db

db=logIntoDatabase()
app= Flask(__name__)

@app.route('/')
def startPage():
    return json.dumps("Hii this page is working and for quering we have 4 endpoints there are" \
           " 1. /loadproject (loads the project details by taking the project_id)" \
           " 2. /getprojectdetails (will get details of datasets and models for the given project_id)" \
           " 3. /getmodeldetails ( will get details of model by taking the model_name)" \
           " 4. /getdatasetdetails ( will get details(this includes models that are trained using this dataset) of dataset by taking the dataset_id)")

@app.route('/loadproject/<project_id>',methods=['GET'])
def loadProject(project_id):
   collection_projects = db['projects']
   if collection_projects.count_documents({'_id': project_id})>0:
       return jsonify({"message": "already loaded the project"})
   url= "http://sentenceapi2.servers.nferx.com:8015/tagrecorder/v3/projects/"+project_id
   response=(requests.get(url).json())
   if(response["success"]):
       data={}
       data['_id']=response['result']['project']['_id']
       data['associated_datasets']=response['result']['project']['associated_datasets']
       data['models']=response['result']['project']['models']
       collection_projects.insert_one(data)

       collection_models=db['models']
       collection_models.insert_many(data['models'])

       for dataset in data['associated_datasets']:
           dataset['used_for_training_models']=[]
       collection_datasets = db['datasets']
       collection_datasets.insert_many(data['associated_datasets'])

       for model in data['models']:
           for dataset_used in model['datasets_used']:
               collection_datasets.update_one({'_id':dataset_used['dataset_id']},{'$push': {'used_for_training_models':model['model_name']}})
       return jsonify({"message":"succesfully loaded the project"})
   else:
      return jsonify({"message":"given project_id is invalid"})

@app.route('/getprojectdetails/<project_id>',methods=['GET'])
def getProjectDetails(project_id):
    collection=db['projects']
    if collection.count_documents({'_id':project_id})>0:
        return jsonify(collection.find_one({'_id':project_id}))
    else:
        return jsonify({'message':"first please load the project"})

@app.route('/getmodeldetails/<model_name>',methods=['GET'])
def getModelDetails(model_name):
    collection=db['models']
    if collection.count_documents({'model_name':model_name})>0:
        return jsonify(collection.find_one({'model_name':model_name},projection={'_id':False}))
    else:
        return jsonify({'message':"entered model name does not exist"})

@app.route('/getdatasetdetails/<dataset_id>',methods=['GET'])
def getDatasetsDetails(dataset_id):
    collection=db['datasets']
    if collection.count_documents({'_id':dataset_id})>0:
        return jsonify(collection.find_one({'_id':dataset_id}))
    else:
        return jsonify({'message':"entered dataset_id  does not exist or info related to given dataset_id not available"})

if __name__ == '__main__':
   app.run(debug= True)