# app.py
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from config import Config
from routes.auth.auth import authentification
from utils.collections import Medecin_collection, Patient_collection, Alertes, Discussions

app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)

print("MONGO_URI:", app.config['MONGO_URI'])
print("Mongo DB:", mongo.db)

# Route d'accueil pour vérifier que tout fonctionne
@app.route('/')
def index():
    return "Hello, Flask & MongoDB!"

if __name__ == "__main__":
    Medecin_collection(mongo)
    Patient_collection(mongo)
    Alertes(mongo)
    Discussions(mongo)
    authentification(app, mongo)
    app.run(debug=True)
