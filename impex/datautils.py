import csv
import random
import string
import os


class DataUtils:

    @staticmethod
    def get_random(liste):
        return liste[random.randint(0, len(liste)-1)]

    @staticmethod
    def generer_code_postal():
        return random.choice(string.ascii_uppercase) + random.choice(string.digits) + \
            random.choice(string.ascii_uppercase) + ' ' + random.choice(string.digits) + \
            random.choice(string.ascii_uppercase) + random.choice(string.digits)

    @staticmethod
    def lire_prenoms():
        prenoms = DataUtils.lire_input('prenoms.txt')
        for i in range(0, len(prenoms)):
            prenoms[i] = prenoms[i].lower().capitalize()
        return prenoms

    @staticmethod
    def generer_utilisateurs_csv(nombre):
        with open('./data/utilisateurs.csv', mode='w', newline='') as csv_file:
            champs = ['email', 'mdp', 'nom', 'prenom', 'type', 'adresse_no', 'adresse_rue', 'adresse_ville',
                      'adresse_prov', 'adresse_pays', 'adresse_cp']
            emails = DataUtils.generer_emails(nombre)
            pwds = DataUtils.generer_mots_de_passe(nombre)
            noms = DataUtils.lire_input('noms.txt')
            prenoms = DataUtils.lire_prenoms()
            rues = DataUtils.lire_input('rues.txt')
            villes = DataUtils.lire_input('villes.txt')
            writer = csv.DictWriter(csv_file, fieldnames=champs)
            writer.writeheader()
            for i in range(0, nombre):
                writer.writerow({'email': DataUtils.get_random(emails), 'mdp': DataUtils.get_random(pwds),
                                 'nom': DataUtils.get_random(noms), 'prenom': DataUtils.get_random(prenoms),
                                 'type': random.choices(['admin', 'client'], weights=[5, 95], k=1)[0],
                                 'adresse_no': random.randint(1, 1024), 'adresse_rue': DataUtils.get_random(rues),
                                 'adresse_ville': DataUtils.get_random(villes), 'adresse_prov': 'QC',
                                 'adresse_pays': 'CA', 'adresse_cp': DataUtils.generer_code_postal()})

    @staticmethod
    def lire_input(nom_fichier):
        items = []
        with open('./input/' + nom_fichier, 'r') as fichier:
            for ligne in fichier:
                ligne = ligne.rstrip(os.linesep)
                items.append(ligne)
        return items

    @staticmethod
    def generer_emails(nombre):
        emails = []
        mots = DataUtils.lire_input('emails.txt')
        for i in range(0, nombre):
            email = mots[random.randint(0, len(mots)-1)] + str(random.randint(1, 999)) + '@tp2.com'
            emails.append(email)
        return emails

    @staticmethod
    def generer_mots_de_passe(nombre):
        pwds = []
        chars = [x for x in string.ascii_letters]
        chars.extend([x for x in string.digits])
        for i in range(0, nombre):
            pwds.append(''.join(random.choices(chars, k=8)))
        return pwds

    @staticmethod
    def generer_geoloc():
        lat = random.uniform(47.000000, 51.000000)
        long = random.uniform(-71.000000, -79.000000)
        return lat, long

    @staticmethod
    def generer_chalets_csv(nombre):
        with open('./data/chalets.csv', mode='w', newline='') as csv_file:
            champs = ["id", "nom", "url_image", "geo_lat", "geo_long"]
            chalets = DataUtils.lire_input('noms_chalet.txt')
            images = DataUtils.lire_input('chalets_images.txt')
            writer = csv.DictWriter(csv_file, fieldnames=champs)
            writer.writeheader()
            for i in range(0, nombre):
                lat, long = DataUtils.generer_geoloc()
                writer.writerow({'id': 1000+i, 'nom': chalets[i], 'url_image': DataUtils.get_random(images),
                                 'geo_lat': lat, 'geo_long': long})


DataUtils.generer_utilisateurs_csv(750)
DataUtils.generer_chalets_csv(52)

