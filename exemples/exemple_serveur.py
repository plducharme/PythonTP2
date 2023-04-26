import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class Zoo:

    def __init__(self):
        self.__enclos = {}

    @property
    def enclos(self):
        return self.__enclos

    def ajout_enclos(self, nom):
        if nom in self.__enclos.keys():
            raise ValueError('Enclos existant')
        self.__enclos[nom] = []

    def ajout_animal(self, enclos, nom):
        if enclos not in self.__enclos.keys():
            raise ValueError('Enclos inexistant')
        self.__enclos[enclos].append(nom)


# Classe permettant de gérer les requêtes envoyées par le client
class TPBaseHTTPRequestHandler(BaseHTTPRequestHandler):

    # variable de classe, initialise notre Zoo
    zoo = Zoo()

    # Point d'entrée pour toutes les requêtes de type GET
    def do_GET(self):
        # self.headers contient tous les entêtes de la requête
        headers = self.headers
        # contient le chemin d'accès de la ressource demandé ex: /enclos/...
        path = self.path
        print(path)
        # Gère les chemin d'accès (path) de type GET /enclos/{nom de l'enclos}
        if path.startswith('/enclos/'):
            # permet d'aller chercher le {nom de l'enclos}
            enclos = path.split('/')[2]
            # appelle l'objet zoo pour aller chercher le contenu de l'enclos
            content = 'Enclos: ' + enclos + ' -> ' + str(self.zoo.enclos[enclos])
            # Renvoyer le code 200 pour dire au client que c'est un succès
            self.send_response(200)
            # Si on avait des entêtes à renvoyer au client, on les ajouterait avant la prochaine ligne
            self.end_headers()
            self.wfile.write(bytes(content, 'utf-8'))
        else:
            # Gère le cas ou le chemin d'accès n'est pas trouvé
            # On pourrait aussi gérer les erreurs
            self.send_response(500, 'enclos non trouve')
            self.end_headers()

    # Permet de gérer l'ajout d'enclos ou l'ajout d'animaux dans un enclos
    def do_POST(self):
        # Chemin d'accès retourné par la requête
        path = self.path
        # Cas d'ajout un enclos
        if path == '/enclos':
            # L'entête content-length contient la longueur du contenu du corps de la requête POST
            content_length = int(self.headers['Content-Length'])
            # lecture entiere du corps du POST
            body = self.rfile.read(content_length)
            # Lecture du body json vers un dictionnaire Python
            json_str = json.loads(body)
            try:
                # Appel de la méthode de zoo pour ajouter un enclos
                self.zoo.ajout_enclos(json_str['nom'])
                self.send_response(200)
            except ValueError:
                # La méthode de zoo a fait un raise d'une exception
                self.send_response(500, 'Enclos existant')
            self.end_headers()
        # Cas ajout d'animal dans un enclos
        elif path.startswith('/enclos/'):
            # Aller chercher le nom de l'enclos
            enclos = path.split('/')[2]
            # Entête indiquant le nombre d'octets (bytes) à lire
            content_length = int(self.headers['Content-Length'])
            # lecture entiere du corps du POST
            body = self.rfile.read(content_length)
            # Lecture du body json vers un dictionnaire Python
            json_str = json.loads(body)
            # Appel de la méthode de zoo pour ajouter un animal
            self.zoo.ajout_animal(enclos, json_str['nom'])
            # HTTP status 200 OK
            self.send_response(200)
            self.end_headers()


# classe du serveur
class ServeurTest:
    @staticmethod
    def run(serveur_class=HTTPServer, serveur_port=8000, handler_class=TPBaseHTTPRequestHandler):
        # le serveur va écouter sur localhost sur le port passé en paramètre
        serveur_adresse = ('localhost', serveur_port)
        # Les requêtes vont être gérées par handler_class passé en paramètre (notre class TPBaseHTTPRequestHandler
        # par défaut)
        httpd = serveur_class(serveur_adresse, handler_class)
        # Écoute pour des requêtes jusqu'à ce qu'on arrête le serveur
        httpd.serve_forever()


ServeurTest.run()
