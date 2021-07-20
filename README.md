# Flask and MongoDB assignmnet
### Task: 
Create a flask application which will use below given project service endpint and make a GET API call to project service. From the response of the API, you have to extract the information related to associated datasets and models and make separate documents for all the datasets and all the models. \
Now create new database with your name inside below given Mongo and create new appropriate collections. Now store the new datasets and models documnets in these collections.

### Expectations: 
You have to give one API endpoint, which will take the project ID and will do all the above processing such that new documnets are stored in new collection.\
Now give two more API endpoints which can be used to fetch the informantion related to datasets and models based on following filters:
- project_id: give all the datasets and models related to a project
- database_id: give the info for that dataset_id
- model_id: give the info for that model_id

An API which will take dataset_id and give the list of models which have been trained using that dataset

### Submission:
Clone this repo in your local and make a new branch with your name, update the readme with the details related to how to use the application. Now commit the changes and push it. Please mention the information related to the implementation and used collections/document designs etc. Do not add any information above ------------ line of this readme file.

### Required Details:
#### Project Service Endpoint: 
``` http://sentenceapi2.servers.nferx.com:8015/tagrecorder/v3/projects/{project_id} ``` \
  e.g.: `http://sentenceapi2.servers.nferx.com:8015/tagrecorder/v3/projects/607e2bb4383fa0b9dc012ba6`

#### bMongoDB Related Info: 
- Host: mongo.servers.nferx.com/
- Credentials: use the credentials you have received in the mail.

#### Test Projects IDs: 
- 5fd1e3d98ba062dffa513175
- 5fd1ead68ba062dffa5204fc
- 601bcdbeb8a45f4f8185185f
- 605db7f1dd043f7dbfd6c4a1
- 607e2bb4383fa0b9dc012ba6

###### You can always reach out to Sairam Bade or Kuldeep on slack in case of any doubt. Good Luck!
---------------------------------------------
#Your readme goes here :)

**Database details**

Mongo server (host) : mongo.servers.nferx.com

database name : yaswanth

Collections : projects, datasets, models

The reason behind having three collections is because of the kind of queries we have on our database
- getProjectDetails
- getDatasetDetails
- getModelDetails
- loadProjectDetails
- 
**User Credentials**

Add your user credentials to the Credentials.py file before running the application. (MONGO_USER and MONGO_PASSWORD) Also modify port number, if necessary.

