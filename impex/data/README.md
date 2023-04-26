# utilisateurs.csv
- email
  - email de l'utilisateur, identifiant unique
- mdp
  - mot de passe, en texte clair (non-encrypté, ne devrait pas être sauvegardé sous cette forme)
- nom
  - Nom de famille de l'utilisateur, pris de la base de données publique du Gouvernement du Québec, https://statistique.quebec.ca/fr/produit/tableau/les-1-000-premiers-noms-de-famille-selon-le-rang-quebec
- prenom
  - Prenom de l'utilisateur, pris de la base de données publique du Gouvernement du Québec, https://www.retraitequebec.gouv.qc.ca/fr/services-en-ligne-outils/banque-de-prenoms/Pages/banque-de-prenoms.aspx
- type
  - type de l'utilisateur: 'client' ou 'admin'
- adresse_no
  - No d'adresse civique, généré aléatoirement entre 1 et 1024
- adresse_rue
  - Nom de rue, pris de la base de données publique sur la toponymie du Gouvernement du Québec, https://toponymie.gouv.qc.ca/ct/toposweb/odonymes.aspx
- adresse_ville
  - Nom de la ville, pris de la base de données publique sur la toponymie du Gouvernement du Québec, https://toponymie.gouv.qc.ca/ct/toposweb/odonymes.aspx
- adresse_prov
  - Province, constante -> 'QC'
- adresse_pays
  - Pays, constante -> 'CA'
- adresse_cp
  - Code Postal, généré aléatoirement sous le format canadien 'H0H 0H0' 
# chalets.csv
- id
  - identifiant unique, integer  
- nom
  - Nom de l'emplacement idyllique, provient d'un blog proposant des noms pour des chalets (lien perdu, sera crédité si retrouvé)
- url_image
  - url de l'image du chalet, pris à partir de https://unsplash.com/fr/licence
geo_lat
    - latitude, généré aléatoirement entre 47.000000 et 51.000000 (entre Château-Richer et Mont-Valin sur la carte lorsque la longitude est de -71.000000) 
geo_long
    - longitude, généré aléatoirement entre -71.000000 et -79.000000 (entre Château-Richer et Rivière-Kipawa sur la carte lors que la latitude est 47.000000)
# disponibilites.xml
Attribut chalet.id: id du chalet pour lequel on défini une plage de disponibilités
Attribut plage.id: id de la plage de disponibilité (correspond à une semaine)