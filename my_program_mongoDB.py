"""
Program created out of tutorial at https://qxf2.com/blog/getting-started-with-mongodb-and-python/
Qxf2 Services: Utility script to connect to MongoDB
NOTE: This was written up for a blog post/tutorial
We use a cleaned up and more robust version at clients
"""

import pymongo

class Mongo_Driver:
    "Class to connect to MongoDB"
    def __init__(self,host,port):
        "Constructor"
        self.host = host
        self.port = port


    def connect(self,database,username,password,auth_mechanism=None):
        "Connect to MongoDB database"
        #src: https://docs.mongodb.org/manual/core/authentication/#security-authentication-mechanisms
        if auth_mechanism is None:
            self.auth_mechanism = "SCRAM"#default authMechanism=SCRAM for mongoDB version 4.0 , change if required
        else:
            self.auth_mechanism = auth_mechanism

        #Construct the connection URI "mongodb://user:password@hostnameOrIP:port/database?authMechanism=MONGODB-CR"
        self.uri = "mongodb://"+username+":"+password+"@"+self.host+":"+self.port+"/"+database+"?"+"authMechanism="+self.auth_mechanism
        self.client = pymongo.MongoClient(self.uri)
        self.db = None
        result_flag = False
        try:
            if database in self.client.database_names():
                self.db = self.client[database]
            if self.db is not None:
                result_flag = True
        except Exception as e:
            print ('\nException when connecting to Mongo instance')
            print ('PYTHON SAYS:')
            print (e)
            print ('\n')

        return result_flag


    def connect2(self,database,username,password):
        "Another way to connect to the database"
        self.uri = self.host+":"+self.port
        self.client = pymongo.MongoClient(self.uri)
        self.db = self.client[database]
        result_flag = self.db.authenticate(username,password)

        return result_flag


    def insert_document(self,document,collection_name):
        "Insert a document into a collection"
        result_flag = False
         try:
            self.collection = self.get_collection(collection_name)
            self.collection.insert(document)
        except Exception as e:
            print ('\nException in insert_document')
            print ('PYTHON SAYS:')
            print (e)
            print ('\n')
        else:
            result_flag = True

        return result_flag


    def get_collection(self,collection_name):
        "Return the collection object with name collection_name"
        self.collection = None
        try:
            self.collection = self.db[collection_name]
            #for document in self.collection.find():
             #   print(document)

        except Exception as e:
            print ("Collection %s not found"%collection_name)

        return self.collection


    def update_document(self,doc_key,doc_update,collection_name):
        "Update a document based on its key"
        result_flag = False
        try:
            self.collection = self.get_collection(collection_name)
            result_obj = self.collection.update(doc_key,doc_update)
            if result_obj['updatedExisting'] is True:
                result_flag = True
        except Exception as e:
            print ('\nException in update_document')
            print ('PYTHON SAYS:')
            print (e)
            print ('\n')

        return result_flag


    def delete_document(self,doc_key,collection_name):
        "Delete a given document"
        result_flag = False
        try:
            self.collection = self.get_collection(collection_name)
            result_obj = self.collection.remove(doc_key)
            if result_obj['n'] is 1:
                result_flag = True
        except Exception as e:
            print ('\nException in delete_document')
            print ('PYTHON SAYS:')
            print (e)
            print ('\n')
        else:
            return result_flag


#---EXAMPLE USAGE---
if __name__=='__main__':
    'user created with role:readWrite - Example: db.createUser({"user":"raji1","pwd":"Testdb123","roles":[{"role":"readWrite" OR "dbAdmin","db":"qxf2"}]}) '
    #mongo connection string parameters (read these from config file)
    host = "127.0.0.1"
    port = "27017"
    user = "preedhi"
    password = "Testdb123"
    db_name = "qxf2"
    collection = "Employees"
    document = {"name":"Jack","address":[{"area":"NRI Layout","city":"blr","pin":"560016","state":"KA"},{"area":"NRI Layout","city":"blr","pin":"560016","state":"KA"}],"contact":"90000000006","emp_id":"0007"}
    document_key = {"name":"Jack"}

    #initialize mongo driver object
    mongo_obj = Mongo_Driver(host,port)

    #connect to a db
    if mongo_obj.connect(db_name,user,password) is True:
        print ("DB authorization successful")
        #insert document
        if mongo_obj.insert_document(document,collection) is True:
            print ("insert document successful")
        else:
            print ("insert document unsuccessful")

        #update document
        if mongo_obj.update_document(document_key,document,collection) is True:
            print ("update document successful")
        else:
           print ("update document unsuccessful")

        #get data from collection
        """
        if mongo_obj.get_collection(collection) is True:
            print ("Data found in the collection:",collection)
        else:
            print("Collection has no data!\n")
        """

        #delete document
        if mongo_obj.delete_document(document_key,collection) is True:
            print ("delete document successful")
        else:
            print ("delete document unsuccessful")
    else:
        print ("DB authorization unsuccessful")

                                                                         