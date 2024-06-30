# app.py
from flask import Flask, request, jsonify
import os
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
    #app.run(debug=True)
    port = int(os.environ.get('PORT', 5000))  # Utilise le port spécifié par Render, ou 5000 par défaut
    app.run(host='0.0.0.0', port=port)
