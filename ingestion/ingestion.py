import couchdb
import requests
import json
from datetime import date
from fastapi import FastAPI
from pydantic import BaseModel
from collections import ChainMap
import schemas

app = FastAPI()
couch = couchdb.Server('http://admin:01061970@localhost:5984')
db_name = ['camera', 'user', 'event']
for i in db_name:
    if i in couch:
        break
    else:
        db = couch.create('camera')
        db1 = couch.create('user')
        db2 = couch.create('event')

db_cam = couch['camera']
db_user = couch['user']
db_event = couch['event']
'''
class Camera(BaseModel):
    camID: int
    camURL: str
    # registartionDate: date
    logPath: str
    status: str
    analyticalMode: str
    streamURL: str
    reason: str

class User(BaseModel):
    userID: int
    username: str
    camID: int
    # registartionDate: date
    embeddingID: str
    # timestamp :datetime
    registrationMeta: str
    # validity:datetime

class Event(BaseModel):
    eventID: int
    camID: int
    userID: int
    analytcalMeta: str
    # timestamp :datetime
'''

@app.put('/camera')
def create_camera_doc(camera: schemas.Camera):
    db_cam.save(camera.dict())
    return camera


@app.get('/camera')
def get_camera():
    rows = db_cam.view('_all_docs', include_docs=True)
    data = [row['doc'] for row in rows]
    return data

@app.put('/user')
def create_user_doc(user: schemas.User):
    db_user.save(user.dict())
    return user

@app.get('/user')
def get_user():
    rows = db_user.view('_all_docs', include_docs=True)
    data = [row['doc'] for row in rows]
    return data

@app.put('/event')
def create_event_doc(event: schemas.Event):
    db_event.save(event.dict())
    return event

@app.get('/event')
def get_user():
    rows = db_event.view('_all_docs', include_docs=True)
    data = [row['doc'] for row in rows]
    return data


