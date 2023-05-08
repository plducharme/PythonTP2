import requests


# Classe permettant de générer des requêtes vers le serveur
class ClientServeurZoo:

    def __init__(self, url_base):
        self.__url_base = url_base
        self.__post_headers = {'Content-Type': 'text/json'}

    def ajout_enclos(self, nom):
        json_body = '{"nom": "' + nom + '"}'
        req = requests.post(self.__url_base + '/enclos', data=json_body)
        print(req.status_code)
        print(req.content)

    def ajout_animal(self, enclos, nom):
        json_body = '{"nom": "' + nom + '" }'
        req = requests.post(self.__url_base + '/enclos/' + enclos, data=json_body)
        print(req.status_code)
        print(req.content)

    def liste_animaux_enclos(self, enclos):
        req = requests.get(self.__url_base + '/enclos/' + enclos)
        print(req.status_code)
        print(req.content)


client = ClientServeurZoo('http://localhost:8000')
client.ajout_enclos('laurentien')
client.ajout_enclos('antarctic')
client.ajout_animal('laurentien', 'Bill le castor')
client.ajout_animal('laurentien', 'Paulette la belette')
client.ajout_animal('laurentien', 'Karen le furet')
client.ajout_animal('antarctic', 'Sylvain le pingouin')
client.liste_animaux_enclos('laurentien')
client.liste_animaux_enclos('antarctic')
