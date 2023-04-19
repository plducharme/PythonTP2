# Serveur
## Rôle
Permet d'effectuer les opérations CRUD pour les réservations
## Requis fonctionnels
- Basé sur le protocole HTTP
1) GET /reservation/{reservationId}: Retourne l'information sur la réservation
2) GET /reservations/{email}: Retourne toutes les réservations de l'utilisateur
3) POST /reservation: Ajoute une réservation, doit être un administrateur
4) PUT /reservation/{reservationId}: remplace la réservation, doit être administrateur
5) DELETE /reservation/{reservationId}: Supprime la réservation
6) POST /utilisateur: Ajoute un utilisateur
7) GET /reservations: si administrateur, renvoyé toutes les réservations triées par ordre de
reservationId (pas de sort, votre choix d'algorithme). Peut prendre un paramètre "limite=" pour limiter le nombre de résultats renvoyés
8) POST /chalet: Ajoute un chalet
9) GET /chalet/{chaletId}: Retourne les informations pour ce chalet
- le format de communication est JSON (voir plus bas)
- En cas de réussite, le code HTTP renvoyé sera 200
- En cas d'erreur, le code HTTP renvoyé sera 542
  - Le contenu de la réponse doit inclure la raison de l'erreur
- Un administrateur peut effectuer toutes les opérations
- Un utilisateur régulier peut seulement consulter ses propres réservations
- Les réservations devront être persistées dans le répertoire "voute" en format gzip avec la nomenclature:
{reservationId}.res.gz
  - Le format de sauvegarde sera une sérialisation binaire de votre objet représentant la réservation
- Implémenter un cache pour retourner les informations de réservations plus rapidement
  - Ne pas oublier d'invalider ou modifier le cache lors de modifications
- Le serveur devra persister les utilisateurs à partir de la liste chargée via le sous-système "impex"
  - Les mots de passes ne doivent pas être sauvegardés en clair
    - Utiliser une fonction de hachage pour persister/vérifier le mot de passe
    - Le serveur doit vérifier l'authentification de l'utilisateur et s'assurer qu'il a le bon type (rôle) pour l'action requise 
- Lors du lancement du serveur, utiliser le module impex pour initialiser les données initiales
  - Se définir un utilisateur système (administrateur) pour le chargement initial

## Formats JSON
### Utilisateurs
  `{
    "utilisateur": {
      "email": "test@test.com",
      "mot_de_passe": "123456",
      "nom": "Laforce",
      "prenom": "Chantelle",
      "type": "client",
      "adresse": {
        "no_civique": 4,
        "rue": "rue des fleurs",
        "ville": "Ste-Eulalie",
        "province": "QC",
        "pays": "CA",
        "code_postal": "H0H 0H0"
      }
    }
  }`
### Réservations (ajout/modification/retrait)
`{
  "reservation": {
    "id": 12345678,
    "chalet": {
      "id": 1234,
      "nom": "Doux Repos",
      "url_image": "https://s3.amazonaws.com/imagescloud/images/medias/hebergement/camp-rustique-hiver.jpg",
      "geolocalisation" {
        "latitude": 51.470544,
        "longitude": -2.588658
      }
    }
    "utilisateur": {
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
    }
  }       
}`

### Réservation (Recherche)
`{
  "reservations": [liste d'objets JSON "reservation"  ]
}`
### Chalets
`{
  "chalet": {
      "id": 1234,
      "nom": "Doux Repos",
      "url_image": "https://s3.amazonaws.com/imagescloud/images/medias/hebergement/camp-rustique-hiver.jpg",
      "geolocalisation" {
        "latitude": 51.470544,
        "longitude": -2.588658
  }
}`

