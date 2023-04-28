# impex
##  Rôle
Permet d'importer et exporter des données du serveur SuperChalets
## Requis fonctionnels
- Importer le module client
- Lire un fichier CSV contenant les utilisateurs, leur type d'utilisateur, leur mot de passe; voir README.md dans le répertoire data pour le format
  - Appeler le serveur (via le client) pour créer les utilisateurs
- Lire un fichier CSV contenant les Chalets
  - Appeler le serveur (via le client) pour les créer
- Lire un fichier XML contenant les disponibilités de réservations pour les chalets
  - Appeler le serveur (via le client) pour les créer
- Lire un fichier XML contenant les réservations
  - Appeler le serveur (via le client) pour les créer
- Les données sont dans le répertoire "data"
- Implémenter une méthode statique "def export_csv(utilisateur_json) pour exporter les données d'un objet JSON "utilisateur" dans un fichier "export_{timestamp}.csv" dans le format CSV
  - ex:  `"utilisateur": {
      "email": "a@a.com",
      "nom": "Laforce",
      "prenom": "Chantelle",
      "adresse": {
        "no_civique": 4,
        "rue": "rue des fleurs",
        "ville": "Ste-Eulalie",
        "province": "QC",
        "pays": "CA",
        "code_postal": "H0H 0H0"
      }
    }`
  - J'en profite pour vous rappeler de regarder le code de datautils; juste une intuition...
- Implémenter une méthode statique pour exporter les données d'un objet JSON "reservation" dans un fichier "export_{timestamp}.xml" dans le format XML
  - ex: `"reservation": {
    "id": 12345678,
    "chalet": {
      "id": 1234,
      "nom": "Doux Repos",
      "url_image": "https://s3.amazonaws.com/imagescloud/images/medias/hebergement/camp-rustique-hiver.jpg",
      "geolocalisation" {
        "latitude": 51.470544,
        "longitude": -2.588658
      },
      "plages": [32, 33]
    }`
  - ex: `<reservation id="1000000"><chalet>1000</chalet><utilisateur>order313@tp2.com</utilisateur><plages><plage>46</plage></plages></reservation>`
  - Il suffit de chercher au bon endroit et adapter
  - Implémenter une fonction (pas une méthode)  `def executer()` qui contient le code à appeler pour l'import des données vers le serveur 

## datautils
module permettant de générer des données de tests dans le répertoire /data
- Aucun développement à y faire
