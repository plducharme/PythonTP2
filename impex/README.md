# impex
##  Rôle
Permet d'importer et exporter des données du serveur SuperChalets
## Requis fonctionnels
- Lire un fichier CSV contenant les utilisateurs, leur type d'utilisateur (Enum), leur mot de passe; voir README.md dans le répertoire data pour le format
  - Appeler le serveur (via le client) pour créer les utilisateurs
- Lire un fichier CSV contenant les Chalets
  - Appeler le serveur (via le client) pour les créer
- Lire un fichier XML contenant les disponibilités de réservations pour les chalets
  - Appeler le serveur (via le client) pour les créer
- Lire un fichier XML contenant les réservations et appeler le serveur pour les créer si les plages sont disponibles
  - Envoyer une erreur "ReservationError" et écrire 'reservationId' dans un fichier "erreurs.log"
- Les données sont dans le répertoire "data"
- Implémenter une méthode pour exporter les données de réservations dans un fichier "export_{timestamp}.csv" dans le format CSV
  - Doit se faire via l'appel au serveur (via le client)
- Implémenter une méthode pour exporter les données de réservations dans un fichier "export_{timestamp}.json" dans le format JSON
  - Doit se faire via l'appel au serveur (via le client)
## datautils
module permettant de générer des données de tests
- va être mise-à-jour au cours de la semaine (PyCharm: "Git->Update Project->Merge incoming...->Ok")