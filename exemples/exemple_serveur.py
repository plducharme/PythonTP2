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

class TPBaseHTTPRequestHandler(BaseHTTPRequestHandler):

    # variable de classe
    zoo = Zoo()
    def do_GET(self):
        headers = self.headers
        path = self.path
        if path.startswith('/enclos/'):
            enclos = path.split('/')[2]
            content = 'Enclos: ' + enclos + ' -> ' + str(self.zoo.enclos[enclos])
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(content, 'utf-8'))
        else:
            self.send_response(500, 'enclos non trouve')
            self.end_headers()

    def do_POST(self):
        path = self.path
        if path == '/enclos':
            content_length = int(self.headers['Content-Length'])
            # lecture entiere du corps du POST
            body = self.rfile.read(content_length)
            json_str = json.loads(body)
            try:
                self.zoo.ajout_enclos(json_str['nom'])
                self.send_response(200)
            except ValueError:
                self.send_response(500, 'Enclos existant')
            self.end_headers()
        elif path.startswith('/enclos/'):
            enclos = path.split('/')[2]
            content_length = int(self.headers['Content-Length'])
            # lecture entiere du corps du POST
            body = self.rfile.read(content_length)
            json_str = json.loads(body)
            self.zoo.ajout_animal(enclos, json_str['nom'])
            self.send_response(200)
            self.end_headers()


class ServeurTest:

    @staticmethod
    def run(serveur_class=HTTPServer, serveur_port=8000, handler_class=TPBaseHTTPRequestHandler):
        serveur_adresse = ('', serveur_port)
        httpd = serveur_class(serveur_adresse, handler_class)
        httpd.serve_forever()


serveur = ServeurTest.run()