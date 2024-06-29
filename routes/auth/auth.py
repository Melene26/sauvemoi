from flask import request, jsonify
import datetime

def authentification(app, mongo):
    # inscription des médecins (ça marche)
    @app.route('/register/medecin', methods=['POST'])
    def register_medecin ():
        data = request.get_json()

        email = mongo.db.Medecin_collection.find_one({"email": data["email"]})
        if email:
            return jsonify({"error": "Ce mail est déjà utilisé"}), 200
        
        Ville = data.get('ville')
        ville = Ville.lower()

        medecin = {
            "nom" : data.get('nom'),
            "prenom" : data.get('prenom'),
            "birthday" : data.get('birthday'),
            "sexe" : data.get('sexe'),
            "poids" : data.get('poids'),
            "email" : data.get('email'),
            "situation_matrimoniale" : data.get('situation_matrimoniale'),
            "hopital" : data.get('hopital'),
            "ville" : ville,
            "poste" : data.get('poste'),
            "suivi" : data.get('suivi'),
            "matricule" : data.get('matricule'),
            "password" : data.get('password')
        }

        result = mongo.db.Medecin_collection.insert_one(medecin)
        return jsonify({"message": "Utilisateur inscrit avec succès", "user_id": str(result.inserted_id)}), 201

    # inscription des patients (ça marche)
    @app.route('/register/patient', methods=['POST'])
    def register_patient ():
        data = request.get_json()

        email = mongo.db.Patient_collection.find_one({"email": data["email"]})
        if email:
            return jsonify({"error": "Ce mail est déjà utilisé"}), 200

        Ville = data.get('ville')
        ville = Ville.lower()
       
        patient = {
            "nom" : data.get('nom'),
            "prenom" : data.get('prenom'),
            "birthday" : data.get('birthday'),
            "sexe" : data.get('sexe'),
            "poids" : data.get('poids'),
            "email" : data.get('email'),
            "situation_matrimoniale" : data.get('situation_matrimoniale'),
            "situation_professionnelle" : data.get('situation_professionnelle'),
            "situation_financière" : data.get('situation_financière'),
            "numero" : data.get('numero'),
            "ville" : ville,
            "suivi" : data.get('suivi'),
            "password" : data.get('password')
        }

        result = mongo.db.Patient_collection.insert_one(patient)
        return jsonify({"message": "Utilisateur inscrit avec succès", "user_id": str(result.inserted_id)}), 201
    
    # Connexion medecin (ça marche)
    @app.route('/login/medecin', methods = ['POST'])
    def login_medecin():
        data = request.get_json()
        
        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:
            return jsonify({"error": "Email et mot de passe sont requis"}), 400
        
        medecin = mongo.db.Medecin_collection.find_one({"email": email}, {"_id": 0})
        if not medecin:
            return jsonify({"error": "Email ou mot de passe incorrect"}), 401
        check = password == medecin['password']
        if medecin and check:
            return jsonify({"message": "Connexion réussie", "medecin": medecin}), 200
        else:
            return jsonify({"error": "Email ou mot de passe incorrect"}), 401
        

    # Connexion patient (ça ne marche pas encore)
    @app.route('/login/patient', methods = ['POST'])
    def login_patient():
        data = request.get_json()
        
        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:
            return jsonify({"error": "Email et mot de passe sont requis"}), 400
        
        patient = mongo.db.Patient_collection.find_one({"email": email}, {"_id": 0})
        if not patient:
            return jsonify({"error": "Email ou mot de passe incorrect"}), 401
        
        check = password == patient['password']
        if patient and check:
            return jsonify({"message": "Connexion réussie", "patient": patient}), 200
        else:
            return jsonify({"error": "Email ou mot de passe incorrect"}), 401


    # retrouver les hopitaux à partir de la ville (ça marche)
    @app.route('/hopital', methods = ['POST'])
    def fund_hopital():
        data = request.get_json()

        Ville = data.get('ville')
        ville = Ville.lower()
        medecins = mongo.db.Medecin_collection.find({"ville": ville}, {"_id": 0, "hopital": 1})
        hopitaux = [medecin['hopital'] for medecin in medecins]
        
        if hopitaux:
            return jsonify({"hopitaux": hopitaux}), 200
        else:
            return jsonify({"message": "Aucun hôpital trouvé pour cette ville"}), 404

    # activer une alerte
    @app.route('/alerte/activer', methods = ['POST'])
    def alerte_activer():
        data = request.get_json()

        alert = {
            "hopital" : data.get('hopital'),
            "position" : data.get('position'),
            "description" : data.get('description'),
            "informations_suplémentaire" : data.get('infos_sup'),
            "recu" : "non"
        }

        result = mongo.db.Alertes.insert_one(alert)
        return jsonify({"message": "Alerte lancé", "user_id": str(result.inserted_id)}), 201

    # désactiver une alerte
    @app.route('/alerte/desactiver', methods = ['POST'])
    def alerte_desactiver():
        data = request.get_json()

        response = data.get('response')
        if response == True:
            result = mongo.db.Alertes.update_one(
                {'_id': data.get('_id')},
                {'$set': {'recu': "oui"}}
            )
            return jsonify({"message": "Alerte terminé", "user_id": str(result.inserted_id)}), 201
