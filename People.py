from config import *

class People(DynamicModel):
    ID = PrimaryKeyField()
    Name = CharField()
    AGE = IntegerField()
