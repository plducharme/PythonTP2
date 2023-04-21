import csv
import random
import string
import os
import xml.etree.ElementTree as ET


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

    @staticmethod
    def generer_chalets_plages_xml(id_depart, id_fin):
        root = ET.Element('disponibilites')
        for i in range(id_depart, id_fin+1):
            chalet = ET.SubElement(root, 'chalet')
            chalet.attrib = {'id': str(i)}
            for j in range(1, 53):
                dispo = ET.SubElement(chalet, 'plage')
                dispo.attrib = {'id': str(j)}
        with open('./data/disponibilites.xml', 'wb') as dispo_xml:
            dispo_xml.write(ET.tostring(root))

    @staticmethod
    def generer_reservations_xml(id_depart, id_fin):
        root = ET.Element('reservations')
        utilisateurs = DataUtils.load_clients()
        for i in range(id_depart, id_fin+1):
            dispos = [x for x in range(1, 53)]
            for j in range(0, 5):
                reservation = ET.SubElement(root, 'reservation')
                reservation.attrib = {'id': str(i) + str("{:03d}".format(j))}
                chalet = ET.SubElement(reservation, 'chalet')
                chalet.text = str(i)
                utilisateur = ET.SubElement(reservation, 'utilisateur')
                utilisateur.text = DataUtils.get_random(utilisateurs)
                plages = ET.SubElement(reservation, 'plages')
                for k in range(1, random.randint(2, 5)):
                    plage = ET.SubElement(plages, 'plage')
                    plage_no = DataUtils.get_random(dispos)
                    dispos.remove(plage_no)
                    plage.text = str(plage_no)
        with open('./data/reservations.xml', 'wb') as xml_file:
            xml_file.write(ET.tostring(root))

    @staticmethod
    def load_clients():
        utilisateurs = []
        with open('./data/utilisateurs.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for ligne in reader:
                if ligne['type'] == 'client':
                    utilisateurs.append(ligne['email'])
        return utilisateurs


DataUtils.generer_utilisateurs_csv(750)
DataUtils.generer_chalets_csv(52)
DataUtils.generer_chalets_plages_xml(1000, 1052)
DataUtils.generer_reservations_xml(1000, 1052)

