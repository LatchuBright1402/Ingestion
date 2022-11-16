from pydantic import BaseModel

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
