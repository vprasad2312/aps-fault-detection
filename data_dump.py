import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH="/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME='aps'
Collection_name ='sensor'

if __name__=="__main__":
    df= pd.read_csv(DATA_FILE_PATH)
    print (f"Rows and columns: {df.shape}")

    ##Convert data into json so that we can dumo into MongoDB

    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    ##insert converted record to mongoDB

    client[DATABASE_NAME][Collection_name].insert_many(json_record)