def Medecin_collection(mongo):
    if 'Medecin_collection' not in mongo.db.list_collection_names():
        mongo.db.create_collection('Medecin_collection')

def Patient_collection(mongo):
    if 'Patient_collection' not in mongo.db.list_collection_names():
        mongo.db.create_collection('Patient_collection')

def Discussions(mongo):
    if 'Discussions' not in mongo.db.list_collection_names():
        mongo.db.create_collection('Discussions')

def Alertes(mongo):
    if 'Alertes' not in mongo.db.list_collection_names():
        mongo.db.create_collection('Alertes')