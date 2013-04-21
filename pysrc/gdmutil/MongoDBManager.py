#!/usr/bin/python
#filename: MongoDBManager.py
#purpose: simple class to manage the mongodb connection

import pymongo
from pymongo import MongoClient

class MongoDBManager:
  def __init__(self, ip, port):
    self.ip = ip
    self.port = port
    self.connection = MongoClient(ip, port)
    print "MongoDBManager::__init__ initialization complete"

  def sel_db(self, dbname):
    self.db = self.connection[dbname]
    print "MongoDBManager::choose_db "+dbname

  def sel_coll(self, prefix, collectionname):
    print "MongoDBManager::choose_collection "+collectionname
    self.collectionName = prefix + "_"+ collectionname
    self.collection = self.db[self.collectionName]

  def insert_doc(self, data):
    print "MongoDBManager::insert_data to collection "+\
        self.collectionName+" #of rows:"+str(len(data))
    self.collection.insert(data)

  def get_count_of_coll(self):
    return self.collection.count()

  def remove_coll(self):
    if(self.collection.count() > 0):
      print "MongoDBManager::remove_collection "+self.collectionName
      self.collection.remove()
    else:
      print "MongoDBManager::remove_collection "+self.collectionName+\
          " has no rows"

  def retrieve_doc(self, query=None):
    if(self.collectionName == None):
      print "MongoDBManager::retrieve_doc returning empty list"
      return list()
    else:
      docs = list()
      for doc in self.collection.find(query).sort("date",1):
        docs.append(doc)
      return docs


